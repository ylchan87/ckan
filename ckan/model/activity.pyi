from datetime import datetime
from typing import Dict, List, Optional
from sqlalchemy import Table
from ckan.model import domain_object

activity_table: Table
activity_detail_table: Table

class Activity(domain_object.DomainObject):
    id: str
    timestamp: datetime
    user_id: str
    object_id: str
    revision_id: str
    activity_type: str
    data: Dict
    def __init__(
        self,
        user_id: str,
        object_id: str,
        activity_type: str,
        data: Optional[Dict] = ...,
    ) -> None: ...
    @classmethod
    def get(cls, id: str) -> Optional["Activity"]: ...

class ActivityDetail(domain_object.DomainObject):
    id: str
    activity_id: str
    object_id: str
    object_type: str
    activity_type: str
    data: Dict
    def __init__(
        self,
        activity_id: str,
        object_id: str,
        object_type: str,
        activity_type: str,
        data: Optional[Dict] = ...,
    ) -> None: ...
    @classmethod
    def by_activity_id(cls, activity_id: str) -> List["ActivityDetail"]: ...

def user_activity_list(
    user_id: str, limit: int, offset: int
) -> List[Activity]: ...
def package_activity_list(
    package_id: str,
    limit: int,
    offset: int,
    include_hidden_activity: bool = ...,
) -> List[Activity]: ...
def group_activity_list(
    group_id: str, limit: int, offset: int, include_hidden_activity: bool = ...
) -> List[Activity]: ...
def organization_activity_list(
    group_id: str, limit: int, offset: int, include_hidden_activity: bool = ...
) -> List[Activity]: ...
def activities_from_everything_followed_by_user(
    user_id: str, limit: int, offset: int
) -> List[Activity]: ...
def dashboard_activity_list(
    user_id: str, limit: int, offset: int
) -> List[Activity]: ...
def recently_changed_packages_activity_list(
    limit: int, offset: int
) -> List[Activity]: ...
