import re

VALID_SOLR_PARAMETERS = set(
    [
        "q",
        "fl",
        "fq",
        "rows",
        "sort",
        "start",
        "wt",
        "qf",
        "bf",
        "boost",
        "facet",
        "facet.mincount",
        "facet.limit",
        "facet.field",
        "extras",
        "fq_list",
        "tie",
        "defType",
        "mm",
        "df",
    ]
)
QUERY_FIELDS = "name^4 title^4 tags^2 groups^2 text"
solr_regex = re.compile(r'([\\+\-&|!(){}\[\]^"~*?:])')

def escape_legacy_argument(val): ...
def convert_legacy_parameters_to_solr(legacy_params):
    ...

class QueryOptions(dict):

    BOOLEAN_OPTIONS = ...
    INTEGER_OPTIONS = ...
    UNSUPPORTED_OPTIONS = ...
    def __init__(self, **kwargs) -> None: ...
    def validate(self): ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...

class SearchQuery(object):

    def __init__(self) -> None: ...
    @property
    def open_licenses(self): ...
    def get_all_entity_ids(self, max_results=...):
        ...
    def run(
        self,
        query=...,
        terms=...,
        fields=...,
        facet_by=...,
        options=...,
        **kwargs
    ): ...
    __call__ = ...

class TagSearchQuery(SearchQuery):
    def run(self, query=..., fields=..., options=..., **kwargs): ...

class ResourceSearchQuery(SearchQuery):
    def run(self, fields=..., options=..., **kwargs): ...

class PackageSearchQuery(SearchQuery):
    def get_all_entity_ids(self, max_results=...):
        ...
    def get_index(self, reference): ...
    def run(self, query, permission_labels=..., **kwargs):
        ...

def solr_literal(t):
    ...
