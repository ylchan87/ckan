from typing import Dict

from simplejson import RawJSON

class LazyJSONObject(RawJSON, Dict):
    encoded_json: str
    def __init__(self, json_string: str) -> None: ...
