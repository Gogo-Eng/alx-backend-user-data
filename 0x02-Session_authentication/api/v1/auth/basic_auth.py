#!/usr/bin/env python3
"""Basic authentication module for the API
"""
import base64
from typing import TypeVar, Tuple
from models.user import User
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
                    email, rest = decoded_base64_authorization_header.split(
                        ':', 1)
                    pwd = rest
                    return(email, pwd)
                return(None, None)

        return(None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):  # type: ignore
        """returns the User instance based on his email and password.
        """

        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(
            self, request=None) -> TypeVar('User'):  # type: ignore # type:
        """Retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None
        base64_header = self.extract_base64_authorization_header(auth_header)

        if not base64_header:
            return None
        decoded_header = self.decode_base64_authorization_header(base64_header)

        if not decoded_header:
            return None
        extract_credentials = self.extract_user_credentials(decoded_header)

        if not extract_credentials:
            return None
        email, password = extract_credentials

        if not email or not password:
            return None
        return self.user_object_from_credentials(email, password)
