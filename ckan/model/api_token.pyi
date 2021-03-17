from datetime import datetime
from typing import Any, Dict, Optional
from sqlalchemy import Table

from ckan.model import DomainObject, User

api_token_table: Table

class ApiToken(DomainObject):
    id: str
    name: str
    user_id: str
    created_at: datetime
    last_access: Optional[datetime]
    plugin_extras: Dict
    owner: User
    def __init__(self, user_id: str = ..., name: str = ...) -> None: ...
    @classmethod
    def get(cls, id: str) -> Optional["ApiToken"]: ...
    @classmethod
    def revoke(cls, id: str) -> bool: ...
    def touch(self, commit: bool = ...) -> None: ...
    def set_extra(self, key: str, value: Any, commit: bool = ...) -> None: ...
