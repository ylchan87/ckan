from typing import Callable, List, Tuple
from flask import Blueprint

CACHE_PARAMETERS: List[str]
home: Blueprint
@home.before_request
def before_request() -> None: ...
def index() -> str: ...
def about() -> str: ...

util_rules: List[Tuple[str, Callable]]
