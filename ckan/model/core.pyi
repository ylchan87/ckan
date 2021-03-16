from typing import Optional

class State:
    ACTIVE: str
    DELETED: str
    PENDING: str

class StatefulObjectMixin:
    state: Optional[str]
    def delete(self) -> None: ...
    def is_active(self) -> bool: ...
    def undelete(self) -> None: ...
