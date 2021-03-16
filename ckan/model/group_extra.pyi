from sqlalchemy import Table
from ckan.model import core, domain_object

group_extra_table: Table

class GroupExtra(core.StatefulObjectMixin, domain_object.DomainObject):
    id: str
    group_id: str
    key: str
    value: str
    state: str
