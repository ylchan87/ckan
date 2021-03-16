from ckan.model import package as _package
from datetime import datetime
from typing import Collection, Dict, List, Optional, Tuple
from sqlalchemy import Table
from ckan.model import core, domain_object

member_table: Table

class Member(core.StatefulObjectMixin, domain_object.DomainObject):
    id: str
    table_name: str
    table_id: str
    capacity: str
    group_id: str
    state: str
    def __init__(
        self,
        group: Optional[str] = ...,
        table_id: Optional[str] = ...,
        group_id: Optional[str] = ...,
        table_name: Optional[str] = ...,
        capacity: str = ...,
        state: str = ...,
    ) -> None: ...
    @classmethod
    def get(cls, reference: str) -> Optional["Member"]: ...
    def related_packages(self) -> List[_package.Package]: ...

group_table: Table

class Group(core.StatefulObjectMixin, domain_object.DomainObject):
    id: str
    name: str
    title: str
    type: str
    description: str
    image_url: str
    created: datetime
    is_organization: bool
    approval_status: str
    state: str
    def __init__(
        self,
        name: str = ...,
        title: str = ...,
        description: str = ...,
        image_url: str = ...,
        type: str = ...,
        approval_status: str = ...,
        is_organization: bool = ...,
    ) -> None: ...
    @property
    def display_name(self) -> str: ...
    @classmethod
    def get(cls, reference: str) -> Optional["Group"]: ...
    @classmethod
    def all(
        cls, group_type: Optional[str] = ..., state: Tuple[str] = ...
    ) -> Collection["Group"]: ...
    def set_approval_status(self, status: str) -> None: ...
    def get_children_groups(self, type: str = ...) -> List["Group"]: ...
    def get_children_group_hierarchy(
        self, type: str = ...
    ) -> List[Tuple[str, str, str, str]]: ...
    def get_parent_groups(self, type: str = ...) -> List["Group"]: ...
    def get_parent_group_hierarchy(self, type: str = ...) -> List["Group"]: ...
    @classmethod
    def get_top_level_groups(cls, type: str = ...) -> List["Group"]: ...
    def groups_allowed_to_be_its_parent(
        self, type: str = ...
    ) -> List["Group"]: ...
    def packages(
        self,
        with_private: bool = ...,
        limit: Optional[int] = ...,
        return_query: bool = ...,
        context: Optional[Dict] = ...,
    ) -> Collection[_package.Package]: ...
    @classmethod
    def search_by_name_or_title(
        cls,
        text_query: str,
        group_type: Optional[str] = ...,
        is_org: bool = ...,
        limit: int = ...,
    ) -> Collection["Group"]: ...
    def add_package_by_name(self, package_name: str) -> None: ...

MAX_RECURSES: int
HIERARCHY_DOWNWARDS_CTE: str
HIERARCHY_UPWARDS_CTE: str
