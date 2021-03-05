from typing import Dict, Optional, Tuple, Union

import ckan as _ckan
import ckan.logic as logic

import ckan.lib.base as _base
import ckan.logic.validators as logic_validators
import ckan.lib.navl.dictization_functions as dictization_functions
import ckan.lib.helpers as _helpers
import ckan.cli as cli
import ckan.lib.plugins as lib_plugins
import ckan.common as common
from ckan.exceptions import CkanVersionException, HelperError
from ckan.lib.jobs import enqueue as enqueue_job
from ckan.lib import mailer

import ckan.common as converters

# Allow class access to these modules
ckan = _ckan
base = _base

config = common.config
_ = common._
ungettext = common.ungettext
c = common.c
g = common.g
h = _helpers.helper_functions
request = common.request
render = base.render
abort = base.abort
asbool = converters.asbool
asint = converters.asint
aslist = converters.aslist
literal = _helpers.literal
get_action = logic.get_action
chained_action = logic.chained_action
chained_helper = _helpers.chained_helper
get_converter = logic.get_validator
get_validator = logic.get_validator
check_access = logic.check_access
chained_auth_function = logic.chained_auth_function
navl_validate = dictization_functions.validate
missing = dictization_functions.missing
ObjectNotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
ValidationError = logic.ValidationError
StopOnError = dictization_functions.StopOnError
UnknownValidator = logic.UnknownValidator
Invalid = logic_validators.Invalid
DefaultDatasetForm = lib_plugins.DefaultDatasetForm
DefaultGroupForm = lib_plugins.DefaultGroupForm
DefaultOrganizationForm = lib_plugins.DefaultOrganizationForm

error_shout = cli.error_shout

redirect_to = _helpers.redirect_to
url_for = _helpers.url_for
get_or_bust = logic.get_or_bust
side_effect_free = logic.side_effect_free
auth_sysadmins_check = logic.auth_sysadmins_check
auth_allow_anonymous_access = logic.auth_allow_anonymous_access
auth_disallow_anonymous_access = logic.auth_disallow_anonymous_access

mail_recipient = mailer.mail_recipient
mail_user = mailer.mail_user

class _Toolkit:
    @classmethod
    def _render_snippet(
        cls, template: str, data: Optional[Dict] = None
    ) -> _helpers.Markup: ...
    @classmethod
    def _add_template_directory(
        cls, config: common.CKANConfig, relative_path: str
    ) -> None: ...
    @classmethod
    def _add_public_directory(
        cls, config: common.CKANConfig, relative_path: str
    ) -> None: ...
    @classmethod
    def _add_resource(cls, path: str, name: str) -> None: ...
    @classmethod
    def _add_ckan_admin_tabs(
        cls,
        config: common.CKANConfig,
        route_name: str,
        tab_label: str,
        config_var: str = "ckan.admin_tabs",
        icon: Optional[str] = None,
    ) -> None: ...
    @classmethod
    def _requires_ckan_version(
        cls, min_version: str, max_version: Optional[str] = None
    ): ...
    @classmethod
    def _check_ckan_version(
        cls,
        min_version: Optional[str] = None,
        max_version: Optional[str] = None,
    ) -> bool: ...
    @classmethod
    def _get_endpoint(cls) -> Union[Tuple[str, str], Tuple[None, None]]: ...

render_snippet = _Toolkit._render_snippet
add_template_directory = _Toolkit._add_template_directory
add_public_directory = _Toolkit._add_public_directory
add_resource = _Toolkit._add_resource
add_ckan_admin_tab = _Toolkit._add_ckan_admin_tabs
requires_ckan_version = _Toolkit._requires_ckan_version
check_ckan_version = _Toolkit._check_ckan_version
get_endpoint = _Toolkit._get_endpoint
CkanVersionException = CkanVersionException
HelperError = HelperError
enqueue_job = enqueue_job
