from flask import Blueprint

from flask.wrappers import Response

util: Blueprint

def internal_redirect() -> Response: ...
def primer() -> str: ...
