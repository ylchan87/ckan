from typing import Generic, List, Optional, TypeVar
from datetime import datetime as _datetime
import ckan.model as model
from ckan.model import domain_object, meta
from sqlalchemy import Table

Follower = TypeVar("Follower")
Followed = TypeVar("Followed")

class ModelFollowingModel(
    domain_object.DomainObject, Generic[Follower, Followed]
):
    follower_id: str
    object_id: str
    datetime: _datetime
    def __init__(self, follower_id: str, object_id: str) -> None: ...
    @classmethod
    def get(cls, follower_id: str, object_id: str) -> Optional[Followed]: ...
    @classmethod
    def is_following(cls, follower_id: str, object_id: str) -> bool: ...
    @classmethod
    def followee_count(cls, follower_id: str) -> int: ...
    @classmethod
    def followee_list(cls, follower_id: str) -> List[Followed]: ...
    @classmethod
    def follower_count(cls, object_id: str) -> int: ...
    @classmethod
    def follower_list(cls: Follower, object_id) -> Follower: ...

class UserFollowingUser(ModelFollowingModel[model.User, model.User]): ...

user_following_user_table: Table

class UserFollowingDataset(ModelFollowingModel[model.User, model.Package]): ...

user_following_dataset_table: Table

class UserFollowingGroup(ModelFollowingModel[model.User, model.Group]): ...

user_following_group_table: Table
