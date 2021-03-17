from typing import Any, Mapping, Optional
from zope.interface import implementer
from repoze.who.interfaces import IAuthenticator
@implementer(IAuthenticator)
class UsernamePasswordAuthenticator(object):
    def authenticate(
        self, environ: Any, identity: Mapping
    ) -> Optional[str]: ...
