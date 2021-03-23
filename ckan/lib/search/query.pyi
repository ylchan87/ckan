from typing import Any, Dict, List, NoReturn, Optional, Pattern, Set

VALID_SOLR_PARAMETERS: Set[str]
QUERY_FIELDS: str
solr_regex: Pattern

def escape_legacy_argument(val: str) -> str: ...
def convert_legacy_parameters_to_solr(legacy_params: Dict) -> Dict: ...

class QueryOptions(dict):

    BOOLEAN_OPTIONS: List[str]
    INTEGER_OPTIONS: List[str]
    UNSUPPORTED_OPTIONS: List[str]
    def __init__(self, **kwargs) -> None: ...
    def validate(self) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...

class SearchQuery(object):
    def __init__(self) -> None: ...
    @property
    def open_licenses(self) -> List[str]: ...
    def get_all_entity_ids(self, max_results: int = ...):
        List[str]: ...
    def run(
        self,
        query: Optional[str] = ...,
        terms: List[st] = ...,
        fields: Dict = ...,
        facet_by: List[str] = ...,
        options: Optional[Dict] = ...,
        **kwargs: Any
    ) -> NoReturn: ...

class TagSearchQuery(SearchQuery):
    def run(
        self,
        query: Optional[str] = ...,
        fields: Optional[Dict] = ...,
        options: Optional[Dict] = ...,
        **kwargs: Any
    ) -> Dict: ...

class ResourceSearchQuery(SearchQuery):
    def run(
        self, fields: Dict = ..., options: Optional[Dict] = ..., **kwargs: Any
    ) -> Dict: ...

class PackageSearchQuery(SearchQuery):
    def get_all_entity_ids(self, max_results: int = ...) -> List[str]: ...
    def get_index(self, reference: str) -> Dict: ...
    def run(
        self, query: Dict, permission_labels: List[str] = ..., **kwargs: Any
    ) -> Dict: ...

def solr_literal(t: str) -> str: ...
