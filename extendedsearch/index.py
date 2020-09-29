from wagtail.search import index


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
