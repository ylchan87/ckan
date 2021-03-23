import logging
from typing import Any, Dict, Optional, Tuple, Union
import flask
import ckan.logic as logic
from flask.views import MethodView
from flask.wrappers import Response

Blueprint = flask.Blueprint

resource: Blueprint
prefixed_resource: Blueprint

def read(package_type: str, id: str, resource_id: str) -> str: ...
def download(
    package_type: str, id: str, resource_id: str, filename: Optional[str] = ...
) -> Response: ...

class CreateView(MethodView):
    def post(self, package_type: str, id) -> Union[str, Response]: ...
    def get(
        self,
        package_type: str,
        id: str,
        data: Optional[Dict] = ...,
        errors: Optional[Dict] = ...,
        error_summary: Optional[Dict] = ...,
    ) -> str: ...

class EditView(MethodView):
    def post(
        self, package_type: str, id: str, resource_id: str
    ) -> Union[str, Response]: ...
    def get(
        self,
        package_type: str,
        id: str,
        resource_id: str,
        data: Optional[Dict] = ...,
        errors: Optional[Dict] = ...,
        error_summary: Optional[Dict] = ...,
    ) -> str: ...

class DeleteView(MethodView):
    def post(
        self, package_type: str, id: str, resource_id: str
    ) -> Response: ...
    def get(self, package_type: str, id: str, resource_id: str) -> str: ...

def views(package_type: str, id: str, resource_id: str) -> str: ...
def view(
    package_type: str, id: str, resource_id: str, view_id: Optional[str] = ...
) -> str: ...

class EditResourceViewView(MethodView):
    def _prepare(self, id:str, resource_id: str)->Tuple[Dict[str, Any], Dict[str, Any]]:...

    def post(
        self,
        package_type: str,
        id: str,
        resource_id: str,
        view_id: Optional[str] = ...,
    ) -> Union[str, Response]: ...
    def get(
        self,
        package_type: str,
        id: str,
        resource_id: str,
        view_id: Optional[str] = ...,
        post_extra: Optional[Dict] = ...,
    ) -> str: ...

def embedded_dataviewer(
    package_type: str,
    id: str,
    resource_id: str,
    width: int = ...,
    height: int = ...,
) -> str: ...
def datapreview(package_type: str, id: str, resource_id: str) -> str: ...
def register_dataset_plugin_rules(blueprint: Blueprint) -> None: ...
