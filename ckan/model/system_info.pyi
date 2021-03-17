from typing import Any, Optional
from sqlalchemy import Table
from ckan.model import core, domain_object

system_info_table: Table

class SystemInfo(core.StatefulObjectMixin, domain_object.DomainObject):
    id: int
    key: str
    value: str
    state: str
    def __init__(self, key: str, value: str) -> None: ...

def get_system_info(
    key: str, default: Optional[str] = ...
) -> Optional[str]: ...
def delete_system_info(key: str, default: Optional[Any] = ...) -> None: ...
def set_system_info(key: str, value: str) -> Optional[bool]: ...
