#!/usr/bin/env python3

"""Session authentication module for the API
"""
import base64
from typing import TypeVar, Tuple
from models.user import User  # type: ignore
from api.v1.auth.auth import Auth  # type: ignore


class SessionAuth(Auth):
    """Class that handels session auth"""
    pass
