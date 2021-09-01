"""
About wagtail-extendedsearch
============================

Add some more functionality to the wagtail elasticsearch search backend

This plugin adds search capabilities through elasticsearch.
Elasticsearch provides scored search results, facetting, suggestions and
autocomplete.

Features
--------

- filter on fields that are not in the database
- order on fields that are not in the database
- search suggestions when no results are found

This readme is far from done and complete, take care.

Configuration
-------------

- ``WAGTAILSEARCHEXTENSION_NUM_SUGGESTIONS``: Number of suggestions to offer
- ``WAGTAILSEARCHEXTENSION_BOOSTED_FIELDS``: Fields to be boosted
- ``WAGTAILSEARCHEXTENSION_FACET_BUCKET_SIZE``: How many items to allow in a bucket
- ``WAGTAILSEARCHEXTENSION_PAGE_SIZE``: How many items to retrieve from elasticsearc in one go.
- ``WAGTAILSEARCHEXTENSION_MULTIMATCH_TYPE``: How should the score be calculated in a multimatch query
- ``WAGTAILSEARCHEXTENSION_DEFAULT_OPERATOR``: Should all the search terms be present or just one of the search terms? (default=or) change to and if all the search terms should be present.

Facet types
+++++++++++

Facets can be configured using the get_facets classmethod.
This is a list of dictionaries that must look like this::

    [
        {
          "label": "Brand",
          "name": "brand",
          "type": "term",
        }
    ]

Currently 2 facet types are supported
1. ``term``, facets are treated as keywords and counted and matched as such.
2. ``range``, facets are treated as integer ranges, the ``ranges`` parameter must de defined for type range. It can be used to segment the range, eg. ``[10, 100, 100]`` will yield 4 filters ranges, 0-9, 10-99, 100-999 and 1000+

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

For example::

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

"""
from setuptools import setup, find_packages


__version__ = "1.0.7"


setup(
    # package name in pypi
    name="wagtail-extendedsearch",
    # extract version from module.
    version=__version__,
    description="Add some more functionality to the wagtail elasticsearch search backend",
    long_description=__doc__,
    classifiers=[],
    keywords="",
    author="Lars van de Kerkhof",
    author_email="no@way.why",
    url="https://github.com/specialunderwear/wagtail-extendedsearch",
    license="GPL v2.1",
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    namespace_packages=[],
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=["setuptools", "wagtail"],
    # mark test target to require extras.
    extras_require={"test": []},
)
