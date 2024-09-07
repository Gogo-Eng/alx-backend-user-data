#!/usr/bin/env python3

from typing import List, TypeVar
from flask import request


class Auth():
    """Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        return None
