from typing import Any, Dict, List, Literal, Optional, Pattern

INSERT_NEW_SECTIONS_BEFORE_SECTION: str
OPTION_RE: Pattern[str]
SECTION_RE: Pattern[str]

class Changes(dict):
    def add(self, action: Literal["edit", "add"], option: Option) -> None: ...
    def get(self, section, action) -> List: ...

class ConfigToolError(Exception): ...

class Option:
    id: str
    is_commented_out: bool
    key: str
    original: Optional[str]
    section: str
    value: str
    def __init__(
        self,
        section: str,
        key: str,
        value: str,
        is_commented_out: Any,
        original: Optional[str],
    ) -> None: ...
    def comment_out(self) -> None: ...

def calculate_changes(
    existing_options_dict: Dict, desired_options: List[Option], edit: bool
) -> Changes: ...
def calculate_new_sections(
    existing_options: List[Option], desired_options: List[Option]
) -> set: ...
def config_edit(
    config_filepath: str, desired_options: List[Option], edit: bool
) -> None: ...
def config_edit_using_merge_file(
    config_filepath: str, merge_config_filepath: str
) -> None: ...
def config_edit_using_option_strings(
    config_filepath: str,
    desired_option_strings: List[str],
    section: str,
    edit: bool,
) -> None: ...
def make_changes(
    input_lines: List[str],
    new_sections: List[str],
    changes: Dict[str, List[Option]],
) -> list: ...
def parse_config(input_lines: List[str]) -> Dict[str, Option]: ...
def parse_option_string(
    section: str, option_string: str, raise_on_error: bool
) -> Optional[Option]: ...
