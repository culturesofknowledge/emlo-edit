import functools
import logging
from typing import Callable, Iterable

from django.db.models import F
from django.db.models import Q, Lookup, lookups

log = logging.getLogger(__name__)


def create_lookup_query(field, lookup, value) -> Q:
    return Q(**{f'{field}__{lookup}': value})


def create_contains_query(field, value) -> Q:
    return create_lookup_query(field, 'contains', value)


def create_eq_query(field, value) -> Q:
    return Q(**{field: value})


def create_query_factory_by_lookup(lookup):
    def _query_factory(field, value):
        return lookup(F(field), value)

    return _query_factory


def any_queries_match(queries: Iterable[Q]) -> Q:
    return functools.reduce(lambda a, b: a | b, queries, Q())


def all_queries_match(queries: Iterable[Q]) -> Q:
    return functools.reduce(lambda a, b: a & b, queries, Q())


def run_lookup_fn(_fn, _field, _val):
    if (isinstance(_fn, type)
            and issubclass(_fn, Lookup)
            and not isinstance(_field, F)):
        _field = F(_field)

    return _fn(_field, _val)


def create_queries_by_field_fn_maps(field_fn_maps: dict, data: dict) -> list[Q]:
    query_field_values = ((f, data.get(f)) for f in field_fn_maps.keys())
    query_field_values = ((f, v) for f, v in query_field_values if v)
    queries = [run_lookup_fn(field_fn_maps[f], f, v)
               for f, v in query_field_values]
    return queries


def create_queries_by_lookup_field(request_data: dict, lookup_fields: list[str]) -> Iterable[Q]:
    for field_name in lookup_fields:
        field_val = request_data.get(field_name)
        lookup_key = request_data.get(f'{field_name}_lookup')
        if not field_val and lookup_key not in nullable_lookup_keys:
            continue

        if (lookup_fn := choices_lookup_map.get(lookup_key)) is None:
            log.warning(f'lookup fn not found -- [{field_name}][{lookup_key}]')
            continue

        yield run_lookup_fn(lookup_fn, field_name, field_val)


def cond_not(lookup_fn: Callable) -> Callable:
    def _fn(field, val):
        q = lookup_fn(F(field), val)
        if not isinstance(q, Q):
            q = Q(q)
        return ~q

    return _fn


def is_blank(field, val) -> Callable:
    if not isinstance(field, F):
        field = F(field)
    return lookups.IsNull(field, True) | lookups.Exact(field, '')


choices_lookup_map = {
    'contains': lookups.IContains,
    'starts_with': lookups.IStartsWith,
    'ends_with': lookups.IEndsWith,
    'equals': lookups.Exact,
    'not_contain': cond_not(lookups.IContains),
    'not_start_with': cond_not(lookups.IStartsWith),
    'not_end_with': cond_not(lookups.IEndsWith),
    'not_equal_to': cond_not(lookups.Exact),
    'is_blank': is_blank,
    'not_blank': cond_not(is_blank),
    None: lookups.Exact,
    '': lookups.Exact,
}

nullable_lookup_keys = [
    'is_blank', 'not_blank',
]