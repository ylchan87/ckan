from typing import Dict, List

def check_resource_changes(
    change_list: List[Dict], old: Dict, new: Dict, old_activity_id: str
) -> None: ...
def check_metadata_changes(
    change_list: List[Dict], old: Dict, new: Dict
) -> None: ...
