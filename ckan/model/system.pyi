from typing import Any
from ckan.model import domain_object

class System(domain_object.DomainObject):
    name: str
    def purge(self) -> None: ...
    @classmethod
    def by_name(cls, name: Any) -> "System": ...
