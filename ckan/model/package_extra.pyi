from typing import List
from sqlalchemy import Table
from ckan.model import core, domain_object
from ckan.model import package as _package

package_extra_table: Table

class PackageExtra(core.StatefulObjectMixin, domain_object.DomainObject):
    id: str
    package_id: str
    key: str
    value: str
    state: str
    def related_packages(self) -> List[_package.Package]: ...
