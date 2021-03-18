import datetime
import re
from typing import Dict, List

import ckan.model as model
import ckan.logic as logic
import ckan.lib.base as base

from ckan.common import config

def string_to_timedelta(s: str) -> datetime.timedelta: ...
def get_notifications(
    user_dict: dict, since: datetime.datetime
) -> List[Dict]: ...
def send_notification(user: Dict, email_dict: Dict) -> None: ...
def get_and_send_notifications_for_user(user: Dict) -> None: ...
def get_and_send_notifications_for_all_users() -> None: ...
