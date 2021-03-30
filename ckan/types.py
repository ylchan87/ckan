from typing import Any, Callable, Dict, Iterable, List, Optional, TypeVar, Union, overload
from typing_extensions import Protocol, TypedDict

from typing import Collection


Query = Collection
TuplizedKey = TypeVar("TuplizedKey")

DataDict = Dict[str, Any]
Context = Dict[str, Any]
ErrorDict = Dict[str, Union[List[Union[str, Dict[str, Any]]], str]]

class AuthResult(TypedDict):
    success: bool
    msg: Optional[str]

class Validator(Protocol):
    @overload
    def __call__(
        self,
        key: TuplizedKey,
        data: Dict[TuplizedKey, Any],
        errors: ErrorDict,
        context: Context,
    ) -> Any: ...
    @overload
    def __call__(self, value: Any, context: Context) -> Any: ...
    def __call__(self, value) -> Any: ...

Schema = Dict[str, Iterable[Validator]]
ComplexSchemaFunc = Callable[..., Schema]
PlainSchemaFunc = Callable[[], Schema]
