import ckan.model.core
from typing import Any, Callable, Dict, ItemsView, Iterable, List, Tuple, Type

from sqlalchemy import Table

State: Type[ckan.model.core.State]

def get_unique_constraints(table: Table, context: Dict) -> List[list]: ...
def legacy_dict_sort(x) -> Tuple[int, ItemsView]: ...
def obj_dict_dictize(
    obj_dict: Dict, context: Dict, sort_key: Callable
) -> List[dict]: ...
def obj_list_dictize(
    obj_list: List[Any], context: Dict, sort_key: Callable
) -> List[dict]: ...
def table_dict_save(
    table_dict: Dict,
    ModelClass: Any,
    context: Dict,
    extra_attrs: Iterable[str]=...,
) -> Any: ...
def table_dictize(obj: Any, context: Dict, **kw) -> Dict[str, Any]: ...
