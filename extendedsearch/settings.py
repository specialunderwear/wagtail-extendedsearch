from django.conf import settings

ELASTICSEARCH_EXTRA_SETTINGS = getattr(
    settings,
    "WAGTAILSEARCHEXTENSION_ELASTICSEARCH_EXTRA_SETTINGS",
    getattr(settings, "ELASTICSEARCH_EXTRA_SETTINGS", {}),
)
NUM_SUGGESTIONS = getattr(settings, "WAGTAILSEARCHEXTENSION_NUM_SUGGESTIONS", 20)
BOOSTED_FIELDS = getattr(settings, "WAGTAILSEARCHEXTENSION_BOOSTED_FIELDS", {})
FACET_BUCKET_SIZE = getattr(settings, "WAGTAILSEARCHEXTENSION_FACET_BUCKET_SIZE", 10)
PAGE_SIZE = getattr(settings, "WAGTAILSEARCHEXTENSION_PAGE_SIZE", 100)
MULTIMATCH_TYPE = getattr(
    settings, "WAGTAILSEARCHEXTENSION_MULTIMATCH_TYPE", "most_fields"
)
DEFAULT_OPERATOR = getattr(settings, "WAGTAILSEARCHEXTENSION_DEFAULT_OPERATOR", "or")
