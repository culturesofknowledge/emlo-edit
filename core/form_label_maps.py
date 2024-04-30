common_fields = {'change_user': 'Last edited by',
                 'change_timestamp_from': 'Change timestamp from',
                 'change_timestamp_to': 'Change timestamp to'}

field_label_map = {
    'user': common_fields | {
        'username': 'User name',
        'surname': 'Surname',
        'forename': 'Forename',
        'email': 'Email',
        'is_active': 'Active',
        'is_staff': 'Staff',
    },
    'audit': common_fields | {},
    'institution': common_fields | {
        'institution_name': 'Name',
        'institution_city': 'City',
        'institution_country': 'Country',
        'resources': 'Related resources',
        'editors_notes': "Editors' notes",
        'institution_id': 'Repository id',
        'images': 'Images',
    },
    'location': common_fields | {
        'location_name': 'Name',
        'location_id': 'Location id',
        'editors_notes': 'Editors\' notes',
        'sent': 'Sent',
        'recd': 'Received',
        'all_works': 'Sent and received',
        'researchers_notes': 'Researchers\' notes',
        'resources': 'Related resources',
        'latitude': 'Latitude',
        'longitude': 'Longitude',
        'publication_id': 'Publication id',
        'element_1_eg_room': '1. E.g. room',
        'element_2_eg_building': '2. E.g. building',
        'element_3_eg_parish': '3. E.g. parish',
        'element_4_eg_city': '4. E.g. city',
        'element_5_eg_county': '5. E.g. county',
        'element_6_eg_country': '6. E.g. country',
        'element_7_eg_empire': '7. E.g. empire',
        'images': 'Images',
    },
    'person': common_fields | {
        'names_and_titles': 'Names and titles/roles',
        'sent': 'Sent',
        'recd': 'Received',
        'all_works': 'Sent and received',
        'organisation_type': 'Organisation type',
        'editors_notes': 'Editors\' notes',
        'resources': 'Related resources',
        'mentioned': 'Mentioned',
        'roles': 'Professional roles',
        'further_reading': 'Further reading',

        # TODO seem like fields not belong to person
        'element_1_eg_room': '1. E.g. room',
        'element_2_eg_building': '2. E.g. building',
        'element_3_eg_parish': '3. E.g. parish',
        'element_4_eg_city': '4. E.g. city',
        'element_5_eg_county': '5. E.g. county',
        'element_6_eg_country': '6. E.g. country',
        'element_7_eg_empire': '7. E.g. empire',

        'images': 'Images',
        'iperson_id': 'Person or Group ID',
        'other_details': 'Other details',
    },
    'publication': common_fields | {
        'publication_details': 'Publication details',
        'abbrev': 'Abbreviation',
        'publication_id': 'Publication id'},
    'work': common_fields | {
        'description': 'Description',
        'date_of_work_as_marked': 'Date of work as marked',
        'date_of_work_std_year': 'Year',
        'date_of_work_std_month': 'Month',
        'date_of_work_std_day': 'Day',
        'sender_or_recipient': 'Sender or recipient',
        'origin_or_destination': 'Origin or destination',
        'creators_searchable': 'Author/sender',
        'notes_on_authors': 'Notes on authors/senders',
        'addressees_searchable': 'Addressee',
        'places_from_searchable': 'Origin (standardised)',
        'editors_notes': "Editors' notes",
        'places_to_searchable': 'Destination (standardised)',
        'flags': 'Flags',
        'images': 'Images',
        'manifestations_searchable': 'Manifestations',
        'related_resources': 'Related resources',
        'language_of_work': 'Language of work',
        'abstract': 'Abstract',
        'general_notes': 'General notes',
        'original_catalogue': 'Original catalogue',
        'accession_code': 'Source of record',
        'mentioned_searchable': 'People mentioned',
        'origin_as_marked': 'Origin as marked',
        'destination_as_marked': 'Destination as marked',
        'subjects': 'Subjects',
        'keywords': 'Keywords',
        'drawer': 'Drawer',
        'iwork_id': 'Work ID', },
    'lang': {
        'code_639_3': '3-letter language code',
        'code_639_1': 'Alternative 2-letter code',
        'language_name': 'Language name',
        'is_favourite': 'Favourite?',
    },
    'collect_work': {
        'source': 'Source',
        'contact': 'Contact',
        'status': 'Upload status',
        'id_main': 'ID in main database',
        'editors_notes': "Editors' notes",
        'date_of_work': 'Date of work',
        'date_of_work_as_marked': 'Date of work as marked',
        'date_of_work_std_year': 'Year',
        'date_of_work_std_month': 'Month',
        'date_of_work_std_day': 'Day',
        'original_calendar': 'Original calendar',
        'notes_on_date_of_work': 'Notes on date of work',
        'authors': 'Authors',
        'authors_as_marked': 'Authors as marked',
        'notes_on_authors': 'Notes on authors',
        'origin': 'Origin',
        'origin_as_marked': 'Origin as marked',
        'addressees': 'Addressees',
        'addressees_as_marked': 'Addressees as marked',
        'notes_on_addressees': 'Notes on addressees',
        'destination': 'Destination',
        'destination_as_marked': 'Destination as marked',
        'manifestations': 'Manifestations',
        'abstract': 'Abstract',
        'keywords': 'Keywords',
        'languages': 'Languages',
        'subjects': 'Subjects',
        'incipit': 'Incipit',
        'excipit': 'Excipit',
        'people_mentioned': 'People mentioned',
        'notes_on_people_mentioned': 'Notes on people mentioned',
        'places_mentioned': 'Places mentioned',
        'issues': 'Issues',
        'notes_on_letter': 'Notes on letter',
        'resources': 'Related resources',
        'upload_id': 'Upload ID'
    }

}

# "Drawer" under work is a special field in queryable work specific to a so-called Selden work
# it does have a form field but can be searched on nonetheless
