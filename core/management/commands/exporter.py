"""
export data to csv for Emlo-frontend
"""
import itertools
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
from typing import Iterable

from django.core.management import BaseCommand
from django.db.models import Q, Count

import work.views
import location.views
import person.views
from core import constant
from core.constant import REL_TYPE_WAS_SENT_FROM, REL_TYPE_WAS_SENT_TO, REL_TYPE_MENTION
from core.helper import query_utils
from core.helper.view_components import HeaderValues, DownloadCsvHandler
from core.models import CofkUnionRelationshipType, CofkUnionResource, CofkUnionComment, CofkUnionImage
from institution.models import CofkUnionInstitution
from location.models import CofkUnionLocation, create_sql_count_work_by_location
from manifestation.models import CofkUnionManifestation
from person.models import CofkUnionPerson
from work import work_utils
from work.models import CofkUnionWork
from work.work_utils import DisplayableWork


class Command(BaseCommand):
    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-o', '--output_dir', type=str, default='.')

    def handle(self, *args, **options):
        export_all(options['output_dir'])


def get_values_by_names(obj, names: list[str]) -> Iterable:
    for name in names:
        yield getattr(obj, name)


def obj_to_values_by_convert_map(obj, header_list, convert_map: dict) -> Iterable:
    for name in header_list:
        val_fn = convert_map.get(name, lambda o: getattr(o, name))
        yield val_fn(obj)


class ColNamedHeaderValues(HeaderValues):
    def obj_to_values(self, obj) -> Iterable:
        return get_values_by_names(obj, self.get_header_list())


class CommentFrontendCsv(ColNamedHeaderValues):

    def get_header_list(self) -> list[str]:
        return [
            'comment_id',
            'comment',
            'creation_timestamp',
            'creation_user',
            'change_timestamp',
            'change_user',
            'uuid',
            'published',
        ]

    def obj_to_values(self, obj) -> Iterable:
        convert_map = {
            'published': lambda o: 1  # KTODO tobe implement
        }
        return obj_to_values_by_convert_map(obj, self.get_header_list(), convert_map)


class ImageFrontendCsv(ColNamedHeaderValues):

    def get_header_list(self) -> list[str]:
        return [
            'image_id',
            'image_filename',
            'creation_timestamp',
            'creation_user',
            'change_timestamp',
            'change_user',
            'thumbnail',
            'display_order',
            'licence_details',
            'licence_url',
            'credits',
            'uuid',
            'published',
        ]

    def obj_to_values(self, obj) -> Iterable:
        convert_map = {
            'published': lambda o: 1  # KTODO tobe implement
        }
        return obj_to_values_by_convert_map(obj, self.get_header_list(), convert_map)


class InstFrontendCsv(ColNamedHeaderValues):

    def __init__(self):
        self.inst_document_count = self.count_inst_work()

    def count_inst_work(self):
        q = work_utils.q_visible_works(prefix='cofkmanifinstmap__manif__work')
        q &= Q(cofkmanifinstmap__relationship_type=constant.REL_TYPE_STORED_IN)
        queryset = (CofkUnionInstitution.objects.filter(q)
                    .values('institution_id', 'cofkmanifinstmap__manif__work_id')
                    .annotate(Count('cofkmanifinstmap__manif__work_id')))

        c = Counter(row['institution_id'] for row in queryset)
        return c

    def get_header_list(self) -> list[str]:
        return [
            'institution_id',
            'institution_name',
            'institution_synonyms',
            'institution_city',
            'institution_city_synonyms',
            'institution_country',
            'institution_country_synonyms',
            'creation_timestamp',
            'creation_user',
            'change_timestamp',
            'change_user',
            'uuid',
            'address',
            'latitude',
            'longitude',
            'document_count',
            'published',
        ]

    def obj_to_values(self, obj) -> Iterable:
        convert_map = {
            'document_count': lambda o: self.inst_document_count.get(o.institution_id, 0),
            'published': lambda o: 1  # KTODO tobe implement
        }
        return obj_to_values_by_convert_map(obj, self.get_header_list(), convert_map)


class LocationFrontendCsv(ColNamedHeaderValues):

    def get_header_list(self) -> list[str]:
        return [
            'location_id',
            'location_name',
            'latitude',
            'longitude',
            'creation_timestamp',
            'creation_user',
            'change_timestamp',
            'change_user',
            'location_synonyms',
            'element_1_eg_room',
            'element_2_eg_building',
            'element_3_eg_parish',
            'element_4_eg_city',
            'element_5_eg_county',
            'element_6_eg_country',
            'element_7_eg_empire',
            'uuid',
            'sent_count',
            'recd_count',
            'mentioned_count',
            'published',
        ]

    def obj_to_values(self, obj) -> Iterable:
        convert_map = {
            'published': lambda o: 1  # KTODO tobe implement
        }
        return obj_to_values_by_convert_map(obj, self.get_header_list(), convert_map)


class ManifFrontendCsv(ColNamedHeaderValues):

    def get_header_list(self) -> list[str]:
        return [
            'manifestation_id',
            'manifestation_type',
            'id_number_or_shelfmark',
            'printed_edition_details',
            'paper_size',
            'paper_type_or_watermark',
            'number_of_pages_of_document',
            'number_of_pages_of_text',
            'seal',
            'postage_marks',
            'endorsements',
            'non_letter_enclosures',
            'manifestation_creation_calendar',
            'manifestation_creation_date',
            'manifestation_creation_date_gregorian',
            'manifestation_creation_date_year',
            'manifestation_creation_date_month',
            'manifestation_creation_date_day',
            'manifestation_creation_date_inferred',
            'manifestation_creation_date_uncertain',
            'manifestation_creation_date_approx',
            'manifestation_is_translation',
            'language_of_manifestation',
            'address',
            'manifestation_incipit',
            'manifestation_excipit',
            'manifestation_ps',
            'creation_timestamp',
            'creation_user',
            'change_timestamp',
            'change_user',
            'manifestation_creation_date2_year',
            'manifestation_creation_date2_month',
            'manifestation_creation_date2_day',
            'manifestation_creation_date_is_range',
            'manifestation_creation_date_as_marked',
            'opened',
            'uuid',
            'routing_mark_stamp',
            'routing_mark_ms',
            'handling_instructions',
            'stored_folded',
            'postage_costs_as_marked',
            'postage_costs',
            'non_delivery_reason',
            'date_of_receipt_as_marked',
            'manifestation_receipt_calendar',
            'manifestation_receipt_date',
            'manifestation_receipt_date_gregorian',
            'manifestation_receipt_date_year',
            'manifestation_receipt_date_month',
            'manifestation_receipt_date_day',
            'manifestation_receipt_date_inferred',
            'manifestation_receipt_date_uncertain',
            'manifestation_receipt_date_approx',
            'manifestation_receipt_date2_year',
            'manifestation_receipt_date2_month',
            'manifestation_receipt_date2_day',
            'manifestation_receipt_date_is_range',
            'accompaniments',
            'published',
        ]

    def obj_to_values(self, obj) -> Iterable:
        convert_map = {
            'published': lambda o: 1  # KTODO tobe implement
        }
        return obj_to_values_by_convert_map(obj, self.get_header_list(), convert_map)


class PersonFrontendCsv(HeaderValues):
    def get_header_list(self) -> list[str]:
        return [
            'person_id',
            'foaf_name',
            'skos_altlabel',
            'skos_hiddenlabel',
            'person_aliases',
            'date_of_birth_year',
            'date_of_birth_month',
            'date_of_birth_day',
            'date_of_birth',
            'date_of_birth_inferred',
            'date_of_birth_uncertain',
            'date_of_birth_approx',
            'date_of_death_year',
            'date_of_death_month',
            'date_of_death_day',
            'date_of_death',
            'date_of_death_inferred',
            'date_of_death_uncertain',
            'date_of_death_approx',
            'gender',
            'is_organisation',
            'iperson_id',
            'creation_timestamp',
            'creation_user',
            'change_timestamp',
            'change_user',
            'further_reading',
            'date_of_birth_calendar',
            'date_of_birth_is_range',
            'date_of_birth2_year',
            'date_of_birth2_month',
            'date_of_birth2_day',
            'date_of_death_calendar',
            'date_of_death_is_range',
            'date_of_death2_year',
            'date_of_death2_month',
            'date_of_death2_day',
            'flourished',
            'flourished_calendar',
            'flourished_is_range',
            'flourished_year',
            'flourished_month',
            'flourished_day',
            'flourished2_year',
            'flourished2_month',
            'flourished2_day',
            'uuid',
            'flourished_inferred',
            'flourished_uncertain',
            'flourished_approx',
            'sent_count',
            'recd_count',
            'mentioned_count',
            'published',
        ]

    def obj_to_values(self, obj) -> Iterable:
        convert_map = {
            'sent_count': lambda o: getattr(o, 'sent'),
            'recd_count': lambda o: getattr(o, 'recd'),
            'mentioned_count': lambda o: getattr(o, 'mentioned'),
            'published': lambda o: 1  # KTODO what is published and how to define published?
        }
        return obj_to_values_by_convert_map(obj, self.get_header_list(), convert_map)


class RelTypeFrontendCsv(ColNamedHeaderValues):
    def get_header_list(self) -> list[str]:
        return [
            'relationship_code',
            'desc_left_to_right',
            'desc_right_to_left',
            'creation_timestamp',
            'creation_user',
            'change_timestamp',
            'change_user',
            'published',
        ]

    def obj_to_values(self, obj) -> Iterable:
        convert_map = {
            'published': lambda o: 1  # KTODO tobe implement
        }
        return obj_to_values_by_convert_map(obj, self.get_header_list(), convert_map)


class ResourceFrontendCsv(ColNamedHeaderValues):
    def get_header_list(self) -> list[str]:
        return [
            'resource_id',
            'resource_name',
            'resource_details',
            'resource_url',
            'creation_timestamp',
            'creation_user',
            'change_timestamp',
            'change_user',
            'uuid',
            'published',
        ]

    def obj_to_values(self, obj) -> Iterable:
        convert_map = {
            'published': lambda o: 1  # KTODO tobe implement
        }
        return obj_to_values_by_convert_map(obj, self.get_header_list(), convert_map)


class WorkFrontendCsv(ColNamedHeaderValues):
    def get_header_list(self) -> list[str]:
        return [

            'work_id',
            'description',
            'date_of_work_as_marked',
            'original_calendar',
            'date_of_work_std',
            'date_of_work_std_gregorian',
            'date_of_work_std_year',
            'date_of_work_std_month',
            'date_of_work_std_day',
            'date_of_work2_std_year',
            'date_of_work2_std_month',
            'date_of_work2_std_day',
            'date_of_work_std_is_range',
            'date_of_work_inferred',
            'date_of_work_uncertain',
            'date_of_work_approx',
            'authors_as_marked',
            'addressees_as_marked',
            'authors_inferred',
            'authors_uncertain',
            'addressees_inferred',
            'addressees_uncertain',
            'destination_as_marked',
            'origin_as_marked',
            'destination_inferred',
            'destination_uncertain',
            'origin_inferred',
            'origin_uncertain',
            'abstract',
            'keywords',
            'language_of_work',
            'work_is_translation',
            'incipit',
            'explicit',
            'ps',
            'original_catalogue',
            'accession_code',
            'work_to_be_deleted',
            'iwork_id',
            'editors_notes',
            'edit_status',
            'relevant_to_cofk',
            'creation_timestamp',
            'creation_user',
            'change_timestamp',
            'change_user',
            'uuid',
            'published',
        ]

    def obj_to_values(self, obj) -> Iterable:
        convert_map = {
            'published': lambda o: 1  # KTODO tobe implement
        }
        return obj_to_values_by_convert_map(obj, self.get_header_list(), convert_map)


"""

==> cofk_union_relationship.csv <==
'relationship_id',
'left_table_name',
'left_id_value',
'relationship_type',
'right_table_name',
'right_id_value',
'relationship_valid_from',
'relationship_valid_till',
'published',
"""


def query_inst():
    q = work_utils.q_visible_works(prefix='cofkmanifinstmap__manif__work')
    q &= Q(cofkmanifinstmap__relationship_type=constant.REL_TYPE_STORED_IN)
    CofkUnionInstitution.objects.filter(q).all()


def create_location_queryset():
    queryset = CofkUnionLocation.objects
    annotate = {
        'sent_count': create_sql_count_work_by_location([REL_TYPE_WAS_SENT_FROM]),
        'recd_count': create_sql_count_work_by_location([REL_TYPE_WAS_SENT_TO]),
        'mentioned_count': create_sql_count_work_by_location([REL_TYPE_MENTION]),
    }
    queryset = query_utils.update_queryset(queryset, CofkUnionLocation, None, annotate=annotate)
    return queryset


def export_all(output_dir: str = '.'):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # ii = CofkUnionInstitution()
    # ii.cofkmanifinstmap_set.filter()
    #
    # w = CofkUnionWork()
    # w.language_set

    settings = [
        # (lambda: CofkUnionComment.objects.iterator(),
        #  CommentFrontendCsv, CofkUnionComment),
        # (lambda: CofkUnionImage.objects.iterator(),
        #  ImageFrontendCsv, CofkUnionImage),
        # (lambda: CofkUnionInstitution.objects.iterator(),
        #  InstFrontendCsv, CofkUnionInstitution),
        # (lambda: create_location_queryset().iterator(),
        #  LocationFrontendCsv, CofkUnionLocation),
        # (lambda: CofkUnionManifestation.objects.iterator(),
        #  ManifFrontendCsv, CofkUnionManifestation),
        # (lambda: person.views.create_queryset_by_queries(CofkUnionPerson, ).iterator(),
        #  PersonFrontendCsv, CofkUnionPerson),
        # (lambda: CofkUnionRelationshipType.objects.iterator(),
        #  RelTypeFrontendCsv, CofkUnionRelationshipType),
        # (lambda: CofkUnionResource.objects.iterator(),
        #  ResourceFrontendCsv, CofkUnionResource),
        # (lambda: work.views.create_queryset_by_queries(DisplayableWork, ).all(),
         (lambda: DisplayableWork.objects.iterator(),
          WorkFrontendCsv, CofkUnionWork),
    ]
    for objects_factory, target_csv_type_factory, model_class in settings:
        csv_path = output_dir / f'{model_class._meta.db_table}.csv'
        print(f'exporting to {csv_path}')
        # d = itertools.islice(objects_factory(), 10)
        d=objects_factory()
        DownloadCsvHandler(target_csv_type_factory()).create_csv_file(
            d,
            csv_path)