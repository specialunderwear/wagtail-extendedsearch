# pylint: disable=unused-import
from wagtail.search.utils import separate_filters_from_query
from itertools import chain, filterfalse
from collections.abc import Mapping, Iterable, Collection


def get_facet_table(facets):
    return {facet["name"]: facet for facet in facets}


def to_float(num):
    try:
        return float(num)
    except ValueError:
        return 0


def unique_everseen(iterable, key=None):
    """List unique elements, preserving order. Remember all elements ever seen.

    >>> list(unique_everseen('AAAABBBCCDAABBB'))
    ['A', 'B', 'C', 'D']
    >>> list(unique_everseen('ABBCcAD', str.lower))
    ['A', 'B', 'C', 'D']
    """
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def merge_dicts(
    target, updates, overwrite=False, multivalue=False, deduplicate_iterables=False
):
    """
    Merge two dicts

    >>> first = {'a': 1, 'b': [1], 'c': {'d': 1, 'e': [2]}}
    >>> second = {'a': 3, 'b': 'hanny', 'c': {'d': 9, 'e': [7], 'f': [99]}, 'g': 8}
    >>> merge_dicts(first, second)
    {'a': 1, 'b': [1, 'hanny'], 'c': {'d': 1, 'e': [2, 7], 'f': [99]}, 'g': 8}

    >>> first = {'a': 1, 'b': [1], 'c': {'d': 1, 'e': [2]}}
    >>> merge_dicts(first, second, multivalue=True)
    {'a': [1, 3], 'b': [1, 'hanny'], 'c': {'d': 1, 'e': [2, 7], 'f': [99]}, 'g': 8}

    >>> first = {'a': 1, 'b': [1], 'c': {'d': 1, 'e': [2]}}
    >>> merge_dicts(first, second, overwrite=True)
    {'a': 3, 'b': [1, 'hanny'], 'c': {'d': 9, 'e': [2, 7], 'f': [99]}, 'g': 8}

    >>> first = {'a': 1, 'b': [1]}
    >>> second = {'b': [1]}
    >>> merge_dicts(first, second)
    {'a': 1, 'b': [1, 1]}

    >>> first = {'a': 1, 'b': [1]}
    >>> second = {'b': [1]}
    >>> merge_dicts(first, second, deduplicate_iterables=True)
    {'a': 1, 'b': [1]}

    """
    for key, value in updates.items():
        if key in target:
            item = target[key]
            if isinstance(item, dict):
                if isinstance(value, Mapping):
                    target[key] = merge_dicts(item, value, overwrite)
                elif overwrite:
                    target[key] = value
                else:
                    raise Exception("can not merge nub")
            elif isinstance(item, list):
                if isinstance(value, str):
                    item.append(value)
                elif isinstance(value, Iterable):
                    item = item + list(value)
                    if deduplicate_iterables:
                        item = list(unique_everseen(item))
                else:
                    item.append(value)
                target[key] = item
            elif multivalue and value != item:  # gather multiple values into list
                target[key] = [item, value]
            elif overwrite:
                target[key] = value
        else:
            target[key] = value

    return target
