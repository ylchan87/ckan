class BasePage(list):
    def __init__(
        self,
        collection,
        page=...,
        items_per_page=...,
        item_count=...,
        sqlalchemy_session=...,
        presliced_list=...,
        url=...,
        **kwargs
    ) -> None: ...
    def __repr__(self): ...
    def pager(
        self,
        format=...,
        page_param=...,
        partial_param=...,
        show_if_single_page=...,
        separator=...,
        onclick=...,
        symbol_first=...,
        symbol_last=...,
        symbol_previous=...,
        symbol_next=...,
        link_attr=...,
        curpage_attr=...,
        dotdot_attr=...,
        **kwargs
    ): ...

class Page(BasePage):
    def pager(self, *args, **kwargs): ...
