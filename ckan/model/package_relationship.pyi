from ckan.types import Query

from typing import Dict, List, Optional, Tuple
from sqlalchemy import Table
from ckan.model import core, domain_object
from ckan.model import package as _package

package_relationship_table: Table

class PackageRelationship(
    core.StatefulObjectMixin, domain_object.DomainObject
):
    id: str
    subject_package_id: str
    object_package_id: str
    type: str
    comment: str
    state: str

    object: _package.Package
    subject: _package.Package

    types: List[Tuple[str, str]] = ...
    types_printable: List[Tuple[str, str]] = ...
    inferred_types_printable: Dict[str, str] = ...
    def as_dict(
        self, package: _package.Package = ..., ref_package_by: str = ...
    ) -> Dict[str, str]: ...
    def as_tuple(
        self, package: _package.Package
    ) -> Tuple[str, _package.Package]: ...
    @classmethod
    def by_subject(
        cls, package: _package.Package
    ) -> 'Query[_package.Package]': ...
    @classmethod
    def by_object(
        cls, package: _package.Package
    ) -> 'Query[_package.Package]': ...
    @classmethod
    def get_forward_types(cls) -> List[str]: ...
    @classmethod
    def get_reverse_types(cls) -> List[str]: ...
    @classmethod
    def get_all_types(cls) -> List[str]: ...
    @classmethod
    def reverse_to_forward_type(cls, reverse_type: str) -> Optional[str]: ...
    @classmethod
    def forward_to_reverse_type(cls, forward_type: str) -> Optional[str]: ...
    @classmethod
    def reverse_type(cls, forward_or_reverse_type: str) -> Optional[str]: ...
    @classmethod
    def make_type_printable(cls, type_: str) -> str: ...
