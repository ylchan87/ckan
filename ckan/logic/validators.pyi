from ckan.logic import Context, ErrorDict
from typing import Any, Container, Dict, TypeVar, overload, Pattern
from typing_extensions import Protocol
import ckan.lib.navl.dictization_functions as df

Invalid = df.Invalid
StopOnError = df.StopOnError
Missing = df.Missing
missing = df.missing

TuplizedKey = TypeVar("TuplizedKey")

class Validator(Protocol):
    @overload
    def __call__(
        self,
        key: TuplizedKey,
        data: Dict[TuplizedKey, Any],
        errors: ErrorDict,
        context: Context,
    ) -> Any: ...
    @overload
    def __call__(self, value: Any, context: Context) -> Any: ...
    def __call__(self, value) -> Any: ...

def owner_org_validator(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def package_id_not_changed(value: Any, context: Context) -> Any: ...
def int_validator(value: Any, context: Context) -> Any: ...
def natural_number_validator(value: Any, context: Context) -> Any: ...
def is_positive_integer(value: Any, context: Context) -> Any: ...
def boolean_validator(value: Any, context: Context) -> Any: ...
def isodate(value: Any, context: Context) -> Any: ...
def no_http(value: Any, context: Context) -> Any: ...
def package_id_exists(value: str, context: Context) -> Any: ...
def package_id_does_not_exist(value: str, context: Context) -> Any: ...
def package_name_exists(value: str, context: Context) -> Any: ...
def package_id_or_name_exists(
    package_id_or_name: str, context: Context
) -> Any: ...
def resource_id_exists(value: Any, context: Context) -> Any: ...
def user_id_exists(user_id: str, context: Context) -> Any: ...
def user_id_or_name_exists(user_id_or_name: str, context: Context) -> Any: ...
def group_id_exists(group_id: str, context: Context) -> Any: ...
def group_id_or_name_exists(reference: str, context: Context) -> Any: ...
def activity_type_exists(activity_type: Any) -> Any: ...

object_id_validators: Dict[str, Validator]

def object_id_validator(
    key: TuplizedKey,
    activity_dict: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...

name_match: Pattern

def name_validator(value: Any, context: Context) -> Any: ...
def package_name_validator(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def package_version_validator(value: Any, context: Context) -> Any: ...
def duplicate_extras_key(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def group_name_validator(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def tag_length_validator(value: Any, context: Context) -> Any: ...
def tag_name_validator(value: Any, context: Context) -> Any: ...
def tag_not_uppercase(value: Any, context: Context) -> Any: ...
def tag_string_convert(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def ignore_not_admin(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def ignore_not_package_admin(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def ignore_not_sysadmin(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def ignore_not_group_admin(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def user_name_validator(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def user_both_passwords_entered(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def user_password_validator(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def user_passwords_match(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def user_password_not_empty(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def user_about_validator(value: Any, context: Context) -> Any: ...
def vocabulary_name_validator(name: str, context: Context) -> Any: ...
def vocabulary_id_not_changed(value: Any, context: Context) -> Any: ...
def vocabulary_id_exists(value: Any, context: Context) -> Any: ...
def tag_in_vocabulary_validator(value: Any, context: Context) -> Any: ...
def tag_not_in_vocabulary(
    key: TuplizedKey,
    tag_dict: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def url_validator(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def user_name_exists(user_name: str, context: Context) -> Any: ...
def role_exists(role: str, context: Context) -> Any: ...
def datasets_with_no_organization_cannot_be_private(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def list_of_strings(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def if_empty_guess_format(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def clean_format(format): ...
def no_loops_in_hierarchy(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def filter_fields_and_values_should_have_same_length(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def filter_fields_and_values_exist_and_are_valid(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def extra_key_not_in_root_schema(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def empty_if_not_sysadmin(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...

email_pattern: Pattern

def email_validator(value: Any, context: Context) -> Any: ...
def collect_prefix_validate(prefix: str, *validator_names) -> Validator: ...
def dict_only(value: Any): ...
def email_is_unique(
    key: TuplizedKey,
    data: Dict[TuplizedKey, Any],
    errors: ErrorDict,
    context: Context,
) -> Any: ...
def one_of(list_of_value: Container) -> Any: ...
def json_object(value: Any) -> Any: ...
def extras_valid_json(extras: Any, context: Context) -> Any: ...
