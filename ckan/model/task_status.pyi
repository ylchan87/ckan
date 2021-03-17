from datetime import datetime
from sqlalchemy import Table
from ckan.model import domain_object

task_status_table: Table

class TaskStatus(domain_object.DomainObject):
    id: str
    entity_id: str
    entuty_type: str
    task_type: str
    key: str
    value: str
    state: str
    error: str
    last_updated: datetime
    @classmethod
    def get(cls, reference: str) -> "TaskStatus": ...
