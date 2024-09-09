#!/usr/bin/env python3
"""Basic authentication module for the API
"""
from api.v1.auth.auth import Auth  # type: ignore
import base64


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

    def decode_base64_authorization_header(
              self, base64_authorization_header: str) -> str:
        """decoded value of a Base64 string
            base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)

            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):  # type: ignore
        """Returns email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header:
            if not isinstance(decoded_base64_authorization_header, str):
                return(None, None)
            if isinstance(decoded_base64_authorization_header, str):
                if ':' in decoded_base64_authorization_header:
                    email = decoded_base64_authorization_header.split(':')[0]
                    pwd = decoded_base64_authorization_header.split(':')[1]
                    return(email, pwd)
                return(None, None)

        return(None, None)
