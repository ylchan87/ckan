from typing import Dict

from ckan.plugins.interfaces import Interface


class IDataPusher(Interface):

    def after_upload(self, context: Dict, resource_dict: Dict, dataset_dict: Dict) -> None: ...
    def can_upload(self, resource_id: str) -> bool: ...
