from ckan.lib.search.index import SearchIndex
from typing import Dict, List, Any, Optional
import ckan.model as model
import ckan.plugins as p
import ckan.logic as logic

from ckan.lib.search.common import (
    SearchIndexError, SearchError, SearchQueryError,
    # make_connection, is_available, SolrSettings
)

def text_traceback() -> str: ...

SUPPORTED_SCHEMA_VERSIONS: List[str]
DEFAULT_OPTIONS: Dict
SOLR_SCHEMA_FILE_OFFSET_MANAGED: str
SOLR_SCHEMA_FILE_OFFSET_CLASSIC: str

def index_for(_type: str) -> SearchIndex: ...
def query_for(_type: str) -> Dict: ...
def dispatch_by_operation(
    entity_type: str, entity: Dict, operation: str
) -> None: ...

class SynchronousSearchPlugin(p.SingletonPlugin):
    def notify(self, entity: Any, operation: str) -> None: ...

def rebuild(
    package_id: Optional[str] = ...,
    only_missing: bool = ...,
    force: bool = ...,
    refresh: bool = ...,
    defer_commit: bool = ...,
    package_ids: Optional[List[str]] = ...,
    quiet: bool = ...,
): ...
def commit() -> None: ...
def check() -> None: ...
def show(package_reference: str) -> Dict: ...
def clear(package_reference: str) -> None: ...
def clear_all() -> None: ...
def check_solr_schema_version(schema_file: Optional[str] = ...) -> bool: ...
