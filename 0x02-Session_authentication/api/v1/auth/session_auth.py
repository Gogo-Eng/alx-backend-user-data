#!/usr/bin/env python3

"""Session authentication module for the API
"""
import uuid
import base64
from typing import TypeVar, Tuple
from models.user import User  # type: ignore
from api.v1.auth.auth import Auth  # type: ignore


class SessionAuth(Auth):
    """Class that handels session auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session method
        """
        if not user_id:
            return
        if type(user_id) is not str:
            return
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user id for session id method
        """
        if not session_id:
            return
        if type(session_id) is not str:
            return
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """current user method
        """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None):
        """deletes the user session
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if not request or not session_id:
            return False
        if user_id:
            del self.user_id_by_session_id[session_id]
            return True
