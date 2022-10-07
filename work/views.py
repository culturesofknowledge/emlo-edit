import logging
from typing import Optional, Type

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from core.constant import REL_TYPE_COMMENT_AUTHOR, REL_TYPE_COMMENT_ADDRESSEE, REL_TYPE_WORK_IS_REPLY_TO, \
    REL_TYPE_WORK_MATCHES, REL_TYPE_COMMENT_DATE
from core.forms import CommentForm, WorkRecrefForm
from core.helper import view_utils, model_utils, recref_utils
from core.helper.view_utils import DefaultSearchView, FullFormHandler
from person.models import CofkUnionPerson
from work.forms import WorkForm, WorkPersonRecrefForm, WorkAuthorRecrefForm, WorkAddresseeRecrefForm, \
    AuthorRelationChoices, AddresseeRelationChoices
from work.models import CofkWorkPersonMap, CofkUnionWork, create_work_id, CofkWorkComment, CofkWorkWorkMap

log = logging.getLogger(__name__)


class WorkFullFormHandler(FullFormHandler):

    def __init__(self, pk, template_name, request_data=None, request=None, *args, **kwargs):
        super().__init__(pk, *args, request_data=request_data, request=request, **kwargs)
        self.template_name = template_name

    def load_data(self, pk, *args, request_data=None, request=None, **kwargs):
        if pk:
            self.work = get_object_or_404(CofkUnionWork, iwork_id=pk)
        else:
            self.work = None
        self.work_form = WorkForm(request_data or None, instance=self.work)

        tmp_work = self.work or CofkUnionWork()

        self.author_formset = WorkAuthorRecrefForm.create_formset_by_records(
            request_data,
            self.work.cofkworkpersonmap_set.iterator() if self.work else [],
            prefix='work_author'
        )

        self.addressee_formset = WorkAddresseeRecrefForm.create_formset_by_records(
            request_data,
            self.work.cofkworkpersonmap_set.iterator() if self.work else [],
            prefix='work_addressee'
        )

        # comments
        self.author_comment_formset = view_utils.create_formset(
            CommentForm, post_data=request_data,
            prefix='author_comment',
            initial_list=model_utils.models_to_dict_list(tmp_work.author_comments),
        )
        self.addressee_comment_formset = view_utils.create_formset(
            CommentForm, post_data=request_data,
            prefix='addressee_comment',
            initial_list=model_utils.models_to_dict_list(tmp_work.addressee_comments),
        )
        self.date_comment_formset = view_utils.create_formset(
            CommentForm, post_data=request_data,
            prefix='date_comment',
            initial_list=model_utils.models_to_dict_list(tmp_work.date_comments),
        )

        # letters
        self.earlier_letter_handler = EarlierLetterRecrefHandler(
            request_data,
            tmp_work.work_from_set.filter(relationship_type=REL_TYPE_WORK_IS_REPLY_TO).iterator())
        self.later_letter_handler = LaterLetterRecrefHandler(
            request_data,
            tmp_work.work_to_set.filter(relationship_type=REL_TYPE_WORK_IS_REPLY_TO).iterator())
        self.matching_letter_handler = EarlierLetterRecrefHandler(
            request_data,
            tmp_work.work_from_set.filter(relationship_type=REL_TYPE_WORK_MATCHES).iterator(),
            name='matching_letter',
            rel_type=REL_TYPE_WORK_MATCHES,
        )

        # self.loc_handler = LocRecrefHandler(
        #     request_data, model_list=self.person.cofkpersonlocationmap_set.iterator(), )
        #
        # self.org_handler = PersonRecrefHandler(request_data, person_type='organisation',
        #                                        person=self.person)
        # self.parent_handler = PersonRecrefHandler(request_data, person_type='parent',
        #                                           person=self.person)
        # self.children_handler = PersonRecrefHandler(request_data, person_type='children',
        #                                             person=self.person)
        #
        # self.employer_handler = PersonRecrefHandler(request_data, person_type='employer',
        #                                             person=self.person)
        # self.employee_handler = PersonRecrefHandler(request_data, person_type='employee',
        #                                             person=self.person)
        # self.teacher_handler = PersonRecrefHandler(request_data, person_type='teacher',
        #                                            person=self.person)
        # self.student_handler = PersonRecrefHandler(request_data, person_type='student',
        #                                            person=self.person)
        # self.patron_handler = PersonRecrefHandler(request_data, person_type='patron',
        #                                           person=self.person)
        # self.protege_handler = PersonRecrefHandler(request_data, person_type='protege',
        #                                            person=self.person)
        # self.other_handler = PersonRecrefHandler(request_data, person_type='other',
        #                                          name='person_other',
        #                                          person=self.person)
        #
        # self.comment_formset = view_utils.create_formset(CommentForm, post_data=request_data,
        #                                                  prefix='comment',
        #                                                  initial_list=model_utils.related_manager_to_dict_list(
        #                                                      self.person.comments), )
        # self.res_formset = view_utils.create_formset(ResourceForm, post_data=request_data,
        #                                              prefix='res',
        #                                              initial_list=model_utils.related_manager_to_dict_list(
        #                                                  self.person.resources), )
        # self.img_handler = ImageHandler(request_data, request and request.FILES, self.person.images)

    def render_form(self, request):

        context = (
                dict(self.all_named_form_formset())
                | self.create_all_recref_context()
        )
        return render(request, self.template_name, context)


def create_work_person_map_if_field_exist(work_form: WorkForm, work, username,
                                          selected_person_id,
                                          rel_type, ):
    selected_person_id = work_form.cleaned_data.get(selected_person_id)
    if not selected_person_id:
        return

    work_person_map = CofkWorkPersonMap()
    work_person_map.person = get_object_or_404(CofkUnionPerson, pk=selected_person_id)
    work_person_map.work = work
    work_person_map.relationship_type = rel_type
    work_person_map.update_current_user_timestamp(username)
    work_person_map.save()

    return work_person_map


class WorkInitView(LoginRequiredMixin, View):

    @staticmethod
    def create_fhandler(request):
        return WorkFullFormHandler(None, 'work/init_form.html',
                                   request_data=request.POST, request=request)

    def resp_after_saved(self, request, fhandler):
        return redirect('work:full_form', fhandler.work_form.instance.iwork_id)

    def post(self, request, *args, **kwargs):
        fhandler = self.create_fhandler(request)
        if is_invalid(fhandler):
            return fhandler.render_form(request)
        save_full_form_handler(fhandler, request)
        return self.resp_after_saved(request, fhandler)

    def get(self, request, *args, **kwargs):
        return self.create_fhandler(request).render_form(request)


class WorkQuickInitView(WorkInitView):
    def resp_after_saved(self, request, fhandler):
        return redirect('work:return_quick_init', fhandler.work_form.instance.iwork_id)


@login_required
def return_quick_init(request, pk):
    work = CofkUnionWork.objects.get(iwork_id=pk)
    return view_utils.render_return_quick_init(
        request, 'Work', work.work_id, work.work_id)  # KTODO work.name


@login_required
def full_form(request, iwork_id):
    fhandler = WorkFullFormHandler(iwork_id, 'work/init_form.html',
                                   request_data=request.POST, request=request)

    if request.method == 'POST':
        if is_invalid(fhandler):
            return fhandler.render_form(request)
        save_full_form_handler(fhandler, request)

        # reload data
        fhandler.load_data(iwork_id, request_data=None, request=request)

    # KTODO
    return fhandler.render_form(request)


def is_invalid(fhandler: WorkFullFormHandler, ):
    # KTODO make this list generic
    form_formsets = [*fhandler.all_form_formset,
                     # fhandler.img_handler.img_form,
                     # fhandler.img_handler.image_formset,
                     ]
    for h in fhandler.all_recref_handlers:
        form_formsets.extend([h.new_form, h.update_formset, ])

    return view_utils.any_invalid_with_log(form_formsets)


def save_multi_rel_recref_formset(multi_rel_recref_formset, work, request):
    _forms = (f for f in multi_rel_recref_formset if f.has_changed())
    for form in _forms:
        form: WorkPersonRecrefForm
        form.create_or_delete(work, request.user.username)


def save_work_comments(work_id, request, comment_formset, rel_type):
    view_utils.save_m2m_relation_records(
        comment_formset,
        lambda c: model_utils.get_or_create(
            CofkWorkComment,
            **dict(work_id=work_id,
                   comment_id=c.comment_id,
                   relationship_type=rel_type)
        ),
        request.user.username,
        model_id_name='comment_id',
    )


def save_full_form_handler(fhandler: WorkFullFormHandler, request):
    # define form_formsets
    # KTODO make this list generic
    form_formsets = [*fhandler.all_form_formset,
                     # fhandler.img_handler.img_form,
                     # fhandler.img_handler.image_formset,
                     ]
    for h in fhandler.all_recref_handlers:
        form_formsets.extend([h.new_form, h.update_formset, ])

    # ----- validate
    if view_utils.any_invalid_with_log(form_formsets):
        return fhandler.render_form(request)

    # ----- save
    work: CofkUnionWork = fhandler.work_form.instance
    if not work.work_id:
        work.work_id = create_work_id(work.iwork_id)
    work.save()
    log.info(f'save work {work}')  # KTODO fix iwork_id plus more than 1

    # handle selected_person_id
    create_work_person_map_if_field_exist(
        fhandler.work_form, work, request.user.username,
        selected_person_id='selected_author_id',
        rel_type=AuthorRelationChoices.CREATED,
    )
    create_work_person_map_if_field_exist(
        fhandler.work_form, work, request.user.username,
        selected_person_id='selected_addressee_id',
        rel_type=AddresseeRelationChoices.ADDRESSED_TO,
    )

    # handle author_formset
    save_multi_rel_recref_formset(fhandler.author_formset, work, request)
    save_multi_rel_recref_formset(fhandler.addressee_formset, work, request)

    # handle comments
    save_work_comments(work.work_id, request, fhandler.author_comment_formset,
                       REL_TYPE_COMMENT_AUTHOR)
    save_work_comments(work.work_id, request, fhandler.addressee_comment_formset,
                       REL_TYPE_COMMENT_ADDRESSEE)
    save_work_comments(work.work_id, request, fhandler.date_comment_formset,
                       REL_TYPE_COMMENT_DATE)

    # handle recref_handler
    for r in fhandler.all_recref_handlers:
        r.maintain_record(request, work)


class WorkSearchView(LoginRequiredMixin, DefaultSearchView):

    @property
    def title(self) -> str:
        return 'Work'

    def get_queryset(self):
        queryset = CofkUnionPerson.objects.all()
        return queryset

    @property
    def return_quick_init_vname(self) -> str:
        return 'work:return_quick_init'


def find_work_rec_name(work_id) -> Optional[str]:
    # KTODO tobe define
    work = CofkUnionWork.objects.get(work_id=work_id)
    return work and work.work_id


class LetterRecrefHandler(view_utils.MultiRecrefHandler):
    def __init__(self, request_data, model_list, name, target_id_name,
                 rel_type='is_reply_to'):
        initial_list = (m.__dict__ for m in model_list)
        initial_list = (recref_utils.convert_to_recref_form_dict(r, target_id_name, find_work_rec_name)
                        for r in initial_list)
        self.rel_type = rel_type
        super().__init__(request_data, name=name, initial_list=initial_list,
                         recref_form_class=WorkRecrefForm)

    @property
    def recref_class(self) -> Type[models.Model]:
        return CofkWorkWorkMap

    def define_work_from_to(self, parent_instance, target_instance):
        """ define which one is work_from, work_to
        :return : work_from, work_to
        """
        raise NotImplementedError()

    def create_recref_by_new_form(self, target_id, parent_instance) -> Optional[models.Model]:
        if not (target_instance := CofkUnionWork.objects.get(work_id=target_id)):
            log.warning(f"create recref fail, work not found -- {target_id} ")
            return None

        work_work: CofkWorkWorkMap = CofkWorkWorkMap()
        work_work.work_from, work_work.work_to = self.define_work_from_to(
            parent_instance, target_instance)
        work_work.relationship_type = self.rel_type
        return work_work


class EarlierLetterRecrefHandler(LetterRecrefHandler):
    def __init__(self, request_data, model_list, name='earlier_letter',
                 rel_type=REL_TYPE_WORK_IS_REPLY_TO):
        super().__init__(request_data, model_list, name=name,
                         target_id_name='work_to_id',
                         rel_type=rel_type, )

    def define_work_from_to(self, parent_instance, target_instance):
        return parent_instance, target_instance


class LaterLetterRecrefHandler(LetterRecrefHandler):

    def __init__(self, request_data, model_list, name='later_letter',
                 rel_type=REL_TYPE_WORK_IS_REPLY_TO):
        super().__init__(request_data, model_list, name=name,
                         target_id_name='work_from_id',
                         rel_type=rel_type)

    def define_work_from_to(self, parent_instance, target_instance):
        return target_instance, parent_instance
