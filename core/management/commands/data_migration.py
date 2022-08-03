import itertools
import logging
import re
import warnings
from argparse import ArgumentParser
from typing import Type

import django.db.utils
import psycopg2
import psycopg2.errors
from django.core.management import BaseCommand
from django.db import connection
from django.db.models import Model
from psycopg2.extras import DictCursor

from core.helper import iter_utils
from core.models import CofkUnionResource
from location.models import CofkUnionLocation

log = logging.getLogger(__name__)


def is_exists(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchone() is not None


def create_query_all_sql(db_table, schema='public'):
    return f'select * from {schema}.{db_table}'


def find_rows_by_db_table(conn, db_table):
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute(create_query_all_sql(db_table))
    results = cursor.fetchall()
    return results


def clone_rows_by_model_class(conn, model_class: Type[Model], check_duplicate_fn=None):
    """ most simple method to copy rows from old DB to new DB
    * assume all column name are same
    * assume no column have been removed
    """
    if check_duplicate_fn is None:
        def check_duplicate_fn(model):
            return model_class.objects.filter(pk=model.pk).exists()

    record_counter = iter_utils.RecordCounter()

    rows = find_rows_by_db_table(conn, model_class._meta.db_table)
    rows = map(dict, rows)
    rows = (model_class(**r) for r in rows)
    rows = itertools.filterfalse(check_duplicate_fn, rows)
    rows = map(record_counter, rows)
    model_class.objects.bulk_create(rows, batch_size=500)
    log_save_records(f'{model_class.__module__}.{model_class.__name__}',
                     record_counter.cur_size())


def log_save_records(target, size):
    print(f'save news records [{target}][{size}]')


class Command(BaseCommand):
    help = 'Copy / move data from selected DB to project db '

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-u', '--user')
        parser.add_argument('-p', '--password')
        parser.add_argument('-d', '--database')
        parser.add_argument('-o', '--host')
        parser.add_argument('-t', '--port')

    def handle(self, *args, **options):
        data_migration(user=options['user'],
                       password=options['password'],
                       database=options['database'],
                       host=options['host'],
                       port=options['port'])
        # main3()


def main3():
    cursor = connection.cursor()
    sql = 'select 1 from cofk_union_location_resources where cofkunionlocation_id = 4835 and cofkunionresource_id = 939258 '
    a = is_exists(connection, sql)
    # cursor.execute(sql)

    # print('aksdjalskjl')
    # pass
    print(a, sql)


def create_stand_relation_col_name(table_name):
    return table_name.replace('_', '') + '_id'


def create_m2m_relationship_by_relationship_table(conn,
                                                  left_model_class: Type[Model],
                                                  right_model_class: Type[Model],
                                                  cur_relation_table_name):
    left_table_name = left_model_class._meta.db_table
    right_table_name = right_model_class._meta.db_table
    left_col = create_stand_relation_col_name(left_table_name)
    right_col = create_stand_relation_col_name(right_table_name)

    def is_duplicate(_left_id, _right_id):
        sql = f'select 1 from cofk_union_location_resources ' \
              f'where {left_col} = {_left_id} and {right_col} = {_right_id} '
        return is_exists(connection, sql)

    query_cursor = conn.cursor()
    sql = 'select left_id_value, right_id_value from cofk_union_relationship ' \
          f" where left_table_name = '{left_table_name}' " \
          f" and right_table_name = '{right_table_name}' "
    print(sql)
    query_cursor.execute(sql)

    values = query_cursor.fetchall()
    values = (_id for _id in values if not is_duplicate(*_id))
    sql_list = (
        (f'insert into {cur_relation_table_name} ({left_col}, {right_col}) '
         f"values ({left_id}, {right_id})")
        for left_id, right_id in values
    )
    record_counter = iter_utils.RecordCounter()

    insert_cursor = connection.cursor()
    for sql in sql_list:
        try:
            insert_cursor.execute(sql)
            record_counter.plus_one()
        except django.db.utils.IntegrityError as e:
            msg = str(e)
            if re.search(r'violates foreign key constraint.+Key .+is not present in table', msg, re.DOTALL):
                log.warning(msg)
            else:
                raise e

    log_save_records(cur_relation_table_name, record_counter.cur_size())


def data_migration(user, password, database, host, port):
    warnings.filterwarnings('ignore',
                            '.*DateTimeField .+ received a naive datetime .+ while time zone support is active.*')

    conn = psycopg2.connect(database=database, password=password,
                            user=user, host=host, port=port)
    print(conn)

    clone_action_fn_list = [
        lambda: clone_rows_by_model_class(conn, CofkUnionLocation),
        lambda: clone_rows_by_model_class(conn, CofkUnionResource),
        lambda: create_m2m_relationship_by_relationship_table(
            conn, CofkUnionLocation, CofkUnionResource,
            f'{CofkUnionLocation._meta.db_table}_resources',
        ),
    ]

    for fn in clone_action_fn_list:
        fn()

    conn.close()
