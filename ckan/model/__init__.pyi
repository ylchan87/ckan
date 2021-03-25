from typing import Any, Callable, Dict, List
from sqlalchemy.engine import Engine
from ckan.model import meta
from ckan.model.meta import (
    Session,
    engine_is_sqlite,
    engine_is_pg,
)
from ckan.model.core import (
    State,
)
from ckan.model.system import (
    System,
)
from ckan.model.package import (
    Package,
    PackageMember,
    PACKAGE_NAME_MIN_LENGTH,
    PACKAGE_NAME_MAX_LENGTH,
    PACKAGE_VERSION_MAX_LENGTH,
    package_table,
    package_member_table,
)
from ckan.model.tag import (
    Tag,
    PackageTag,
    MAX_TAG_LENGTH,
    MIN_TAG_LENGTH,
    tag_table,
    package_tag_table,
)
from ckan.model.user import (
    User,
    user_table,
)
from ckan.model.group import (
    Member,
    Group,
    group_table,
    member_table,
)
from ckan.model.group_extra import (
    GroupExtra,
    group_extra_table,
)
from ckan.model.package_extra import (
    PackageExtra,
    package_extra_table,
)
from ckan.model.resource import (
    Resource,
    DictProxy,
    resource_table,
)
from ckan.model.resource_view import (
    ResourceView,
    resource_view_table,
)
from ckan.model.tracking import (
    tracking_summary_table,
    TrackingSummary,
    tracking_raw_table,
)
from ckan.model.rating import (
    Rating,
    MIN_RATING,
    MAX_RATING,
)
from ckan.model.package_relationship import (
    PackageRelationship,
    package_relationship_table,
)
from ckan.model.task_status import (
    TaskStatus,
    task_status_table,
)
from ckan.model.vocabulary import (
    Vocabulary,
    VOCABULARY_NAME_MAX_LENGTH,
    VOCABULARY_NAME_MIN_LENGTH,
)
from ckan.model.activity import (
    Activity,
    ActivityDetail,
    activity_table,
    activity_detail_table,
)
from ckan.model.term_translation import (
    term_translation_table,
)
from ckan.model.follower import (
    UserFollowingUser,
    UserFollowingDataset,
    UserFollowingGroup,
)
from ckan.model.system_info import (
    system_info_table,
    SystemInfo,
    get_system_info,
    set_system_info,
    delete_system_info,
)
from ckan.model.domain_object import (
    DomainObjectOperation,
    DomainObject,
)
from ckan.model.dashboard import (
    Dashboard,
)
from ckan.model.api_token import (
    ApiToken,
)

DB_CONNECT_RETRIES: int

def init_model(engine: Engine) -> None: ...

class Repository:
    _alembic_ini: str = ...
    tables_created_and_initialised: bool = ...
    metadata: Any
    session: Any
    commit: Callable
    def __init__(self, metadata: Any, session: Any) -> None: ...
    def commit_and_remove(self) -> None: ...
    def init_db(self) -> None: ...
    def clean_db(self) -> None: ...
    def create_db(self) -> None: ...
    def rebuild_db(self) -> None: ...
    def delete_all(self) -> None: ...
    def reset_alembic_output(self) -> None: ...
    def add_alembic_output(self, *args: str) -> None: ...
    def take_alembic_output(self, with_reset: bool = ...) -> List[str]: ...
    def setup_migration_version_control(self) -> None: ...
    def current_version(self) -> str: ...
    def downgrade_db(self, version: str = ...) -> None: ...
    def upgrade_db(self, version: str = ...) -> None: ...
    def are_tables_created(self) -> bool: ...

repo: Repository

def is_id(id_string: str) -> bool: ...
def parse_db_config(config_key: str = ...) -> Dict[str, str]: ...
