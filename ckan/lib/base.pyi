from typing import Any, Dict, Optional
from flask.wrappers import Response

APIKEY_HEADER_NAME_KEY: str
APIKEY_HEADER_NAME_DEFAULT: str

def abort(
    status_code: Optional[int] = ...,
    detail: str = ...,
    headers: Optional[Dict] = ...,
    comment: Optional[str] = ...,
) -> Response: ...
def render_snippet(*template_names: str, **kw: Any) -> str: ...
def render_jinja2(template_name: str, extra_vars: Dict) -> str: ...
def render(template_name: str, extra_vars: Optional[Dict] = ...) -> str: ...

class ValidationException(Exception): ...
