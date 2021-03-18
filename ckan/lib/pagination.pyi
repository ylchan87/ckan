from typing import Any, Callable, Dict, Iterable, Optional

from markupsafe import Markup

class BasePage(list):
    def __init__(
        self,
        collection: Iterable,
        page: int = ...,
        items_per_page: int = ...,
        item_count: Optional[int] = ...,
        sqlalchemy_session: Any = ...,
        presliced_list: bool = ...,
        url: Optional[Callable] = ...,
        **kwargs: Any
    ) -> None: ...
    def __repr__(self) -> str: ...
    def pager(
        self,
        format: str = ...,
        page_param: str = ...,
        partial_param: str = ...,
        show_if_single_page: bool = ...,
        separator: str = ...,
        onclick: Optional[str] = ...,
        symbol_first: str = ...,
        symbol_last: str = ...,
        symbol_previous: str = ...,
        symbol_next: str = ...,
        link_attr: Dict = ...,
        curpage_attr: Dict = ...,
        dotdot_attr: Dict = ...,
        **kwargs: Any
    ) -> Markup: ...

class Page(BasePage):
    def pager(self, *args: Any, **kwargs: Any) -> Markup: ...
