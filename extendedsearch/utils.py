from django.conf import settings


def get_facet_table():
    return {facet["name"]: facet for facet in settings.OSCAR_SEARCH.get("FACETS")}


def to_float(num):
    try:
        return float(num)
    except ValueError:
        return 0
