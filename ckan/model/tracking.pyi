from datetime import datetime
from typing import Dict
from sqlalchemy import Table
from ckan.model import domain_object

tracking_raw_table: Table

tracking_summary_table: Table

class TrackingSummary(domain_object.DomainObject):
    url: str
    package_id: str
    tracking_type: str
    count: int
    running_total: int
    recent_views: int
    tracking_date: datetime
    @classmethod
    def get_for_package(cls, package_id: str) -> Dict[str, int]: ...
    @classmethod
    def get_for_resource(cls, url: str) -> Dict[str, int]: ...
