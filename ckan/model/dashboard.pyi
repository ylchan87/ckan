from datetime import datetime
from sqlalchemy import Table

dashboard_table: Table

class Dashboard(object):
    user_id: str
    activity_stream_last_viewed: datetime
    email_last_sent: datetime
    def __init__(self, user_id: str) -> None: ...
    @classmethod
    def get(cls, user_id: str) -> "Dashboard": ...
