About wagtail-extendedsearch
============================

Add some more functionality to the wagtail elasticsearch search backend

This plugin adds search capabilities through elasticsearch.
Elasticsearch provides scored search results, facetting, suggestions and
autocomplete.

Configuration
-------------

The facets can be configured using the WAGTAILSEARCHEXTENSION_FACETS setting.
This is a list of dictionaries that must look like this::
    [
        {
          "label": "Brand",
          "name": "brand",
          "type": "term",
        }
    ]

Facet types
+++++++++++

Currently 2 facet types are supported
1. ``term``, facets are treated as keywords and counted and matched as such.
2. ``range``, facets are treated as integer ranges, the ``ranges`` parameter
   must de defined for type range. It can be used to segment the range, eg.
   ``[10, 100, 100]`` will yield 4 filters ranges, 0-9, 10-99, 100-999 and 1000+

Facet ordering
++++++++++++++

The default ordering for facets is alphnumerically  (``{"-key", "asc"}``).
The number of facets returned can be changed with the ocyan parameter ``facet_bucket_size``.
By default only 10 facets will be returned. If there are a lot more facets then
10 and you do not want to increase the number of facets it can make a lot of sense
to order by the number of occurrences, this will select the most useful facets.
The ordering can be changed in the facet definition::

    {
      "label": "Brand",
      "name": "brand",
      "type": "term",
      "order": { "_count" : "desc" }
    }

Now the most popular brands will be shown.
For more info, please read https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html#search-aggregations-bucket-terms-aggregation-order

Boosting fields
+++++++++++++++

Boosting field relevance is done by using the WAGTAILSEARCHEXTENSION_BOOSTED_FIELDS
setting::

    "boosted_fields": {
      "upc": 888,
      "title": 777
    }


Tweaking the mapping
--------------------
You can override/extend the elasticsearch settings by using the ELASTICSEARCH_EXTRA_SETTINGS setting

For example:
``
WAGTAILSEARCHEXTENSION_ELASTICSEARCH_EXTRA_SETTINGS = {
    'settings': {
        'analysis': {
            'analyzer': {
                'custom_analyzer': {
                  'type': 'custom',
                  'tokenizer': 'custom_tokenizer',
                  'filter': ['asciifolding', 'ngram']
                }
            },
            'tokenizer': {
                'custom_tokenizer': {
                    'type': 'nGram',
                    'min_gram': 3,
                    'max_gram': 15
                }
            }
        }
    }
}
``
