from ckan.types import Query
from typing import List, Optional, Any
import ckan.lib.maintain as maintain
from sqlalchemy import Table
from ckan.model import core, domain_object, Vocabulary, Package

MAX_TAG_LENGTH: int
MIN_TAG_LENGTH: int
tag_table: Table

class Tag(domain_object.DomainObject):
    id: str
    name: str
    vocabulary_id: str

    package_tags: Query["PackageTag"]
    vacabulary: Optional[Vocabulary]
    def __init__(
        self, name: str = ..., vocabulary_id: Optional[str] = ...
    ) -> None: ...
    def delete(self) -> None: ...
    @classmethod
    def by_id(cls, tag_id: str, autoflush: bool = ...) -> Optional["Tag"]: ...
    @classmethod
    def by_name(
        cls,
        name: str,
        vocab: Optional[Vocabulary] = ...,
        autoflush: bool = ...,
    ) -> Optional["Tag"]: ...
    @classmethod
    def get(
        cls, tag_id_or_name: str, vocab_id_or_name: Optional[str] = ...
    ) -> Optional["Tag"]: ...
    @classmethod
    def all(
        cls, vocab_id_or_name: Optional[str] = ...
    ) -> Query["Tag"]: ...
    @property
    def packages(self) -> List[Package]: ...

class PackageTag(core.StatefulObjectMixin, domain_object.DomainObject):
    id: str
    package_id: str
    tag_id: str
    state: str
    def __init__(
        self,
        package: Optional[Package] = ...,
        tag: Optional[Tag] = ...,
        state: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...
    def related_packages(self) -> List[Package]: ...
