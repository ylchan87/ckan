import ckan.model as model
import ckan.plugins as p
import ckan.logic as logic
from __future__ import print_function
from ckan.lib.search.index import PackageSearchIndex
from ckan.lib.search.query import (
    PackageSearchQuery,
    ResourceSearchQuery,
    TagSearchQuery,
)

def text_traceback(): ...

SUPPORTED_SCHEMA_VERSIONS = ["2.8", "2.9"]
DEFAULT_OPTIONS = {
    "limit": 20,
    "offset": 0,
    "order_by": "rank",
    "return_objects": False,
    "ref_entity_with_attr": "name",
    "all_fields": False,
    "search_tags": True,
    "callback": None,
}
SOLR_SCHEMA_FILE_OFFSET_MANAGED = "/schema?wt=schema.xml"
SOLR_SCHEMA_FILE_OFFSET_CLASSIC = "/admin/file/?file=schema.xml"

def index_for(_type): ...
def query_for(_type): ...
def dispatch_by_operation(entity_type, entity, operation): ...

class SynchronousSearchPlugin(p.SingletonPlugin):
    def notify(self, entity, operation): ...

def rebuild(
    package_id=...,
    only_missing=...,
    force=...,
    refresh=...,
    defer_commit=...,
    package_ids=...,
    quiet=...,
): ...
def commit(): ...
def check(): ...
def show(package_reference): ...
def clear(package_reference): ...
def clear_all(): ...
def check_solr_schema_version(schema_file=...): ...
