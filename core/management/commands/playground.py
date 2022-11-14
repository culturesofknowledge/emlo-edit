import logging

from django.conf import settings
from django.core.management import BaseCommand

from core.forms import CommentForm
from core.helper import email_utils, model_utils, view_utils
from core.models import CofkUnionResource, CofkUnionComment
from location import fixtures
from location.models import CofkUnionLocation

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'playground for try some python code'

    def handle(self, *args, **options):
        main6()

def main6():
    # new_lang_formset = view_utils.create_formset(
    #     LangForm,
    #     prefix='new_lang',
    #     extra=0,
    #     # initial_list=model_utils.models_to_dict_list(comments_query_fn(rel_type))
    # )
    comment_formset = view_utils.create_formset(CommentForm,
                                                prefix='loc_comment',
                                                initial_list=[], )
    breakpoint()
    print(comment_formset.is_valid())
    print(comment_formset.errors)
    # print(new_lang_formset.is_valid())
    # print(new_lang_formset.errors)

    print('xkxjkxjkxjk')


def main1():
    print('yyyyyy')
    res: CofkUnionResource = CofkUnionResource(
        # resource_id = models.AutoField(primary_key=True)
        resource_name='resource_name val',
        resource_details='resource_details val',
        resource_url='resource_url val',
        # creation_timestamp = models.DateTimeField(blank=True, null=True)
        creation_user='creation_user val',
        # change_timestamp = models.DateTimeField(blank=True, null=True)
        change_user='change_user val',
        # uuid = models.UUIDField(blank=True, null=True)
    )
    res.save()

    loc: CofkUnionLocation = CofkUnionLocation.objects.first()
    l = list(loc.resources.iterator())
    print(l)
    loc.resources.add(l[0])
    # loc.resources.add(res)
    # loc.save()

    loc.refresh_from_db()

    print(list(loc.resources.iterator()))
    # x = loc.resources.a
    # print(x)

    # coll_location: CofkCollectLocation = CofkCollectLocation.objects.first()
    # a = coll_location.resources
    # print(coll_location)
    # print(a)


def main2():
    loc_a = fixtures.create_location_a()
    print(loc_a.location_id)
    loc_a.save()
    print(loc_a.location_id)


def main3():
    print(settings.MEDIA_ROOT)

    c = CofkUnionComment()
    c.update_current_user_timestamp('aaa')
    print(c.__dict__)


def main4():
    email_utils.send_email('errorzetabeta@gmail.com', 'testtingingi', 'yoooooooo')
    # You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

    # You can send up to 300 emails/day from this sandbox server.
    # Next, you should add your own domain so you can send 10000 emails/month for free.


def main5():
    result = model_utils.next_seq_safe('xxkks')
    print(result)
