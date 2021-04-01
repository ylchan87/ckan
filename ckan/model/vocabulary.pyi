from sqlalchemy import Table
from ckan.model import domain_object, Tag
from ckan.types import Query

VOCABULARY_NAME_MIN_LENGTH: int
VOCABULARY_NAME_MAX_LENGTH: int
vocabulary_table: Table

class Vocabulary(domain_object.DomainObject):
    id: str
    name: str
    def __init__(self, name: str) -> None: ...
    @classmethod
    def get(cls, id_or_name: str) -> "Vocabulary": ...
    @property
    def tags(self) -> 'Query[Tag]': ...
