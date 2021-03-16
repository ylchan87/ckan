import datetime
from sqlalchemy import Table
from ckan.model import domain_object

MIN_RATING: int
MAX_RATING: int
rating_table: Table

class Rating(domain_object.DomainObject):
    id: str
    user_id: str
    user_ip_address: str
    package_id: str
    rating: float
    created: datetime.datetime
