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
    def document_insert_hook(cls, obj, doc):
        return doc

    @classmethod
    def get_autocomplete_contexts(cls):
        return []

    @classmethod
    def get_facets(cls):
        return []
