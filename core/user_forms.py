from django import forms

from core.form_label_maps import field_label_map
from core.helper import form_serv
from core.helper.form_serv import BasicSearchFieldset, SearchCharField


class UserSearchFieldset(BasicSearchFieldset):
    title = 'User'
    template_name = 'core/component/user_search_fieldset.html'

    username = SearchCharField(
        label=field_label_map['user']['username'],
        help_text='The user name is used to log in to the system.')
    username_lookup = form_serv.create_lookup_field(form_serv.StrLookupChoices.choices)
    surname = SearchCharField(
        label=field_label_map['user']['surname'],
        help_text='The user\'s surname.')
    surname_lookup = form_serv.create_lookup_field(form_serv.StrLookupChoices.choices)
    forename = SearchCharField(
        label=field_label_map['user']['forename'],
        help_text='The user\'s forename.')
    forename_lookup = form_serv.create_lookup_field(form_serv.StrLookupChoices.choices)
    is_active = SearchCharField(
        help_text="Is the user active? Inactive users cannot log in to the system.",
        widget=forms.Select(choices=form_serv.none_zero_one_choices))
    email = SearchCharField(
        label=field_label_map['user']['email'],
        help_text='The user\'s email address.')
    email_lookup = form_serv.create_lookup_field(form_serv.StrLookupChoices.choices)
    is_staff = SearchCharField(
        help_text="Is the user a staff member? Staff members have access to the system's administrative functions.",
        widget=forms.Select(choices=form_serv.none_zero_one_choices))