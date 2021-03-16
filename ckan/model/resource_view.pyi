from typing import Collection, Dict, KeysView, Optional, Tuple
import sqlalchemy as sa
from ckan.model import domain_object

resource_view_table: sa.Table

class ResourceView(domain_object.DomainObject):
    id: str
    resource_id: str
    title: Optional[str]
    description: Optional[str]
    viev_type: str
    order: int
    config: Dict
    @classmethod
    def get(cls, reference: str) -> Optional["ResourceView"]: ...
    @classmethod
    def get_columns(cls) -> KeysView: ...
    @classmethod
    def get_count_not_in_view_types(
        cls, view_types: Collection[str]
    ) -> Collection[Tuple[str, int]]: ...
    @classmethod
    def delete_not_in_view_types(cls, view_types: Collection[str]) -> None: ...
    @classmethod
    def delete_all(cls, view_types: Collection[str] = ...) -> None: ...
