from functools import partial
from typing import (
    Any, Callable, Dict, Iterable, List,
    Mapping, Optional, Tuple, Union,
    TYPE_CHECKING
)
from typing_extensions import Protocol, TypedDict

from sqlalchemy.orm import Session, Query

if TYPE_CHECKING:
    from ckan.model import User


class AlchemySession(Session):
    def __call__(self): ...
    def remove(self) -> None: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def configure(self, **kwargs: Any) -> None: ...


Config = Dict[str, Union[str, Mapping[str, str]]]

TuplizedKey = Tuple[Any, ...]

DataDict = Dict[str, Any]
ErrorDict = Dict[str, Union[List[Union[str, Dict[str, Any]]], str]]

class Context(TypedDict, total=False):
    user: Optional[str]
    model: Optional[Any]
    ignore_auth: Optional[bool]
    auth_user_obj: Optional['User']

class AuthResult(TypedDict, total=False):
    success: bool
    msg: Optional[str]


class ValueValidator(Protocol):
    def __call__(self, value: Any) -> Any: ...

class ContextValidator(Protocol):
    def __call__(self, *, value: Any, context: Context) -> Any: ...
class DataValidator(Protocol):
    def __call__(
        self,
        key: TuplizedKey,
        data: Dict[TuplizedKey, Any],
        errors: ErrorDict,
        context: Context,
    ) -> Any: ...

Validator = Union[ValueValidator, ContextValidator, DataValidator]


Schema = Dict[str, Iterable[Validator]]
ComplexSchemaFunc = Callable[..., Schema]
PlainSchemaFunc = Callable[[], Schema]

AuthFunction = Union[
    Callable[[Context, Optional[DataDict]], AuthResult],
    partial
]
Action = Callable[[Context, DataDict], Dict]
