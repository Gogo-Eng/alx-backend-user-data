#!/usr/bin/env python3
"""Authentication module for the API
"""

from typing import List, TypeVar
from flask import request


class Auth():
    """Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks whether a particular path requires authentication
        """
        if path is None:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """return the Authorization header from the incoming HTTP request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """returns the current user based on the request
        """
        return None
