"""
Subpackage gathering interfaces for Atlas Search collectors.

Collectors return a document representing the metadata results, typically an aggregation over the matching search results.

The Atlas Search aggregation pipeline stage has the following collector:

Collector           Description
facet               Groups query results by values or ranges in specified, faceted fields and returns the count for each of those groups.
"""

from monggregate.search.collectors.facet import (
    DateFacet,
    # Operator
    Facet,
    # Results
    FacetBucket,
    FacetBuckets,
    # String
    FacetName,
    FacetResult,
    Facets,
    NumericFacet,
    # Query
    StringFacet,
)

__all__ = [
    "DateFacet",
    "Facet",
    "FacetBucket",
    "FacetBuckets",
    "FacetName",
    "FacetResult",
    "Facets",
    "NumericFacet",
    "StringFacet",
]
