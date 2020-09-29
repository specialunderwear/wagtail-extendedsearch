def get_facet_table(facets):
    return {facet["name"]: facet for facet in facets}


def to_float(num):
    try:
        return float(num)
    except ValueError:
        return 0
