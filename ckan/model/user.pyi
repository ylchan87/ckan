import datetime
from typing import (
    Any,
    ClassVar,
    Collection,
    Dict,
    Iterable,
    List,
    Optional,
    Pattern,
)
from sqlalchemy import Table
from ckan.model import core, domain_object, Group
from sqlalchemy.sql.schema import Column

def set_api_key() -> Optional[str]: ...

user_table: Table

class User(core.StatefulObjectMixin, domain_object.DomainObject):
    id: str
    name: str
    password: str
    fullname: str
    email: str
    api_key: Optional[str]
    created: datetime.datetime
    reset_key: str
    about: str
    activity_streams_email_notifications: bool
    sysadmin: bool
    state: str
    image_url: str
    plugin_extras: Dict

    VALID_NAME: Pattern
    DOUBLE_SLASH: Pattern
    @classmethod
    def by_email(cls, email: str) -> List["User"]: ...
    @classmethod
    def get(cls, user_reference: str) -> Optional["User"]: ...
    @classmethod
    def all(cls) -> List["User"]: ...
    @property
    def display_name(self) -> str: ...
    @property
    def email_hash(self) -> str: ...
    def get_reference_preferred_for_uri(self) -> str: ...
    def validate_password(self, password: str) -> None: ...
    @classmethod
    def check_name_valid(cls, name: str) -> bool: ...
    @classmethod
    def check_name_available(cls, name: str) -> bool: ...
    def as_dict(self) -> Dict: ...
    def number_created_packages(
        self, include_private_and_draft: bool = ...
    ) -> int: ...
    def activate(self) -> None: ...
    def set_pending(self) -> None: ...
    def is_deleted(self) -> bool: ...
    def is_pending(self) -> bool: ...
    def is_in_group(self, group_id: str) -> bool: ...
    def is_in_groups(self, group_ids: Iterable[str]) -> bool: ...
    def get_group_ids(
        self, group_type: Optional[str] = ..., capacity: Optional[str] = ...
    ) -> List[str]: ...
    def get_groups(
        self, group_type: Optional[str] = ..., capacity: Optional[str] = ...
    ) -> Group: ...
    @classmethod
    def search(
        cls,
        querystr: str,
        sqlalchemy_query: Optional[Any] = ...,
        user_name: Optional[str] = ...,
    ) -> Collection["User"]: ...
    @classmethod
    def user_ids_for_name_or_id(
        cls, user_list: List[str] = ...
    ) -> List[str]: ...
