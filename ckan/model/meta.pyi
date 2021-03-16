from typing import Any, Optional
from sqlalchemy.engine import Engine
import sqlalchemy.orm as orm
from sqlalchemy.orm.scoping import ScopedSession

from sqlalchemy.orm.session import sessionmaker

engine: Optional[Engine]
Session: ScopedSession

create_local_session: sessionmaker
mapper: Any
metadata: Any

def engine_is_sqlite(sa_engine: Optional[Engine] = ...) -> bool: ...
def engine_is_pg(sa_engine: Optional[Engine] = ...) -> bool: ...
