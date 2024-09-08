#!/usr/bin/env python3
"""Basic authentication module for the API
"""
from api.v1.auth.auth import Auth  # type: ignore


class BasicAuth(Auth):
    """Basic authentication class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extracts the Base64 part of the 
        Authorization header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]
