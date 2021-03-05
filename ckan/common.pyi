# (generated with --quick)

import flask.globals
import flask.wrappers
import typing
from typing import Any, FrozenSet, Iterable, Iterator, Type
from werkzeug.datastructures import ImmutableDict
import werkzeug.local

Local: Type[werkzeug.local.Local]
LocalProxy: Type[werkzeug.local.LocalProxy]
MutableMapping: Type[typing.MutableMapping]
c: werkzeug.local.LocalProxy
config: CKANConfig
current_app: flask.globals._FlaskLocalProxy
falsy: FrozenSet[str]
g: werkzeug.local.LocalProxy
local: werkzeug.local.Local
request: CKANRequest
session: werkzeug.local.LocalProxy
truthy: FrozenSet[str]

class CKANConfig(typing.MutableMapping):
    store: dict
    def clear(self) -> None: ...
    def copy(self) -> dict: ...

class CKANRequest(werkzeug.local.LocalProxy):
    params: ImmutableDict

def _(*args, **kwargs) -> Any: ...
def asbool(obj: Any) -> bool: ...
def asint(obj: Any) -> int: ...
def aslist(obj: Any, sep: str, strip: bool) -> List: ...
def is_flask_request() -> bool: ...
def streaming_response(
    data: Iterable, mimetype: str, with_context: bool
) -> flask.wrappers.Response: ...
def ugettext(*args, **kwargs) -> str: ...
def ungettext(*args, **kwargs) -> str: ...
