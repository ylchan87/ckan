import flask.globals
import flask.wrappers
from typing import Any, FrozenSet, Iterable, List, MutableMapping, Optional
from werkzeug.datastructures import ImmutableDict
import werkzeug.local

current_app: flask.globals._FlaskLocalProxy

c: werkzeug.local.LocalProxy
g: werkzeug.local.LocalProxy

local: werkzeug.local.Local

config: CKANConfig

request: CKANRequest
session: werkzeug.local.LocalProxy

truthy: FrozenSet[str]
falsy: FrozenSet[str]

class CKANConfig(MutableMapping):
    store: dict
    def clear(self) -> None: ...
    def copy(self) -> dict: ...

class CKANRequest(werkzeug.local.LocalProxy):
    params: ImmutableDict

def _(*args, **kwargs) -> Any: ...
def ugettext(*args, **kwargs) -> str: ...
def ungettext(*args, **kwargs) -> str: ...
def asbool(obj: Any) -> bool: ...
def asint(obj: Any) -> int: ...
def aslist(obj: Any, sep: Optional[str] = ..., strip: bool = ...) -> List: ...
def is_flask_request() -> bool: ...
def streaming_response(
    data: Iterable, mimetype: str, with_context: bool
) -> flask.wrappers.Response: ...
