import configparser

from typing import Any, Dict, Mapping, Optional, Union

Config = Dict[str, Union[str, Mapping[str, str]]]

class CKANConfigLoader:
    config: Config
    config_file: str
    parser: configparser.ConfigParser
    section: str
    def __init__(self, filename: str) -> None: ...
    def get_config(self) -> Config: ...

def error_shout(exception: Any) -> None: ...
def load_config(ini_path: Optional[str] = ...) -> Config: ...
