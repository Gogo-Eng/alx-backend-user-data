#!/usr/bin/env python3
"""Authentication module for the API
"""

from typing import List, TypeVar
from flask import request
import re


class Auth():
    """Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks whether a particular path requires authentication
        """
        
        if not path.endswith('/'):
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if excluded_path.startswith(excluded_paths[:-1]):
                    if re.fullmatch(excluded_path, path):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """return the Authorization header from the incoming HTTP request
        """
        if request is None:
            return None
        if 'Authorization' in request.headers:
            return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """returns the current user based on the request
        """
        return None
