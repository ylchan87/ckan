import datetime
from typing import Any, Dict, List, Optional
from sqlalchemy import Table
from ckan.model import core, domain_object
from .package import Package

CORE_RESOURCE_COLUMNS: List[str]
resource_table: Table

class Resource(core.StatefulObjectMixin, domain_object.DomainObject):
    id: str
    package_id: str
    url: str
    format: str
    description: str
    hash: str
    position: int
    name: str
    resource_type: str
    mimetype: str
    size: int
    created: datetime.datetime
    last_modified: datetime.datetime
    metadata_modified: datetime.datetime
    cache_url: str
    cache_last_update: datetime.datetime
    url_type: str
    extras: Dict
    state: str

    extra_columns: Optional[List[str]] = ...

    package: Package
    def __init__(
        self,
        url: str = ...,
        format: str = ...,
        description: str = ...,
        hash: str = ...,
        extras: Optional[Dict] = ...,
        package_id: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...
    def as_dict(self, core_columns_only: bool = ...) -> Dict: ...
    def get_package_id(self) -> str: ...
    @classmethod
    def get(cls, reference: str) -> Optional["Resource"]: ...
    @classmethod
    def get_columns(cls, extra_columns: bool = ...) -> List[str]: ...
    @classmethod
    def get_extra_columns(cls) -> List[str]: ...
    @classmethod
    def get_all_without_views(
        cls, formats: List[str] = ...
    ) -> List["Resource"]: ...
    def related_packages(self) -> List[Package]: ...

def resource_identifier(obj: Resource) -> str: ...
