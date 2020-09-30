from wagtail.search import index

# pylint: disable=unused-import
from wagtail.search.index import (
    insert_or_update_object,
    remove_object,
    SearchField,
    AutocompleteField,
    FilterField,
    RelatedFields,
)


class Indexed(index.Indexed):
    @classmethod
    def get_autocomplete_contexts(cls):
        return [
            {
                "name": "status",
                "type": "category",
                "path": "search_productproxy__status_filter",
            }
        ]

    @classmethod
    def get_facets(cls):
        return []
