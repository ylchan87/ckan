from typing import Any, Dict, List, Optional, Union
from flask.blueprints import Blueprint
from flask.wrappers import Response
from six import text_type
from feedgen.feed import FeedGenerator

feeds: Blueprint

ITEMS_LIMIT: Union[str, int]
BASE_URL: Optional[str]
SITE_TITLE: str

class Enclosure(text_type):
    url: str
    length: str
    mime_type: str
    def __init__(self, url: str) -> None: ...

class CKANFeed(FeedGenerator):
    def __init__(
        self,
        feed_title: str,
        feed_link: str,
        feed_description: str,
        language: str,
        author_name: str,
        feed_guid: str,
        feed_url: str,
        previous_page: str,
        next_page: str,
        first_page: str,
        last_page: str,
    ) -> None: ...
    def writeString(self, encoding: str) -> str: ...
    def add_item(self, **kwargs: Any) -> None: ...

def output_feed(
    results: List[Dict],
    feed_title: str,
    feed_description: str,
    feed_link: str,
    feed_url: str,
    navigation_urls: Dict[str, str],
    feed_guid: str,
) -> Response: ...
def group(id: str) -> Response: ...
def organization(id: str) -> Response: ...
def tag(id: str) -> Response: ...
def group_or_organization(obj_dict: Dict, is_org: bool) -> Response: ...
def general() -> Response: ...
def custom() -> Response: ...
