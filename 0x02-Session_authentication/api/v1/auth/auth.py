#!/usr/bin/env python3
"""Authentication module for the API
"""

from os import getenv
from typing import List, TypeVar
from flask import request
import re


class Auth():
    """Authentication class
    """
    def require_auth(
        self, path: str, excluded_paths: List[str]
    ) -> bool:
        """ determines if authentication is required """
        if path is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path = path + '/'
        for pth in excluded_paths:
            if pth[-1] == '*':
                pth = pth[:-1] + '.*'
            if re.fullmatch(pth, path):
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
    
    def session_cookie(self, request=None):
        """session_cookie method
        """
        _my_session_id = getenv('SESSION_NAME')

        if not request:
            return
        return request.cookies.get(_my_session_id)
