#!/usr/bin/env python3

"""Session authentication module for the API
"""
import uuid
import base64
from typing import TypeVar, Tuple
from models.user import User  # type: ignore
from models.user_session import UserSession  # type: ignore
from api.v1.auth.auth import Auth  # type: ignore
from api.v1.auth.session_exp_auth import SessionExpAuth  # type: ignore
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """Class that handels session auth"""

    def create_session(self, user_id=None):
        """Creates and stores a session id for the user
        """
        session_id = super().create_session(user_id)
        UserSession.load_from_file()
        if type(session_id) == str:
            kwargs = {
                'user_id': user_id,
                'session_id': session_id
            }

            user_session = UserSession(**kwargs)
            user_session.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieves the user id of the user associated with
        a given session id.
        """
        if not session_id:
            return

        session = UserSession.search({'session_id': session_id})

        if not session:
            return
        session_info = session[0]

        session_age = datetime.now() - session_info.created_at

        if session_age > timedelta(seconds=self.session_duration):
            return
        return session_info.user_id

    def destroy_session(self, request=None):
        """deletes the user session
        """
        session_id = self.session_cookie(request)
        session = UserSession.search({'session_id': session_id})
        if not request or not session_id:
            return False
        if not session or len(session) <= 0:
            return False
        if session_id:
            del session[0]
            return True
