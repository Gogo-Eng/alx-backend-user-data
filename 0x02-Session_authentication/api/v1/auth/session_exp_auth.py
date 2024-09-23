#!/usr/bin/env python3

"""Session authentication module for the API
"""
import datetime
import os
import uuid
import base64
from typing import TypeVar, Tuple
from models.user import User  # type: ignore
from api.v1.auth.auth import Auth  # type: ignore
from api.v1.auth.session_auth import SessionAuth  # type: ignore


class SessionExpAuth(SessionAuth):
    """class for the expiration date to a session id"""
    def __init__(self):
        self.session_duration = int(os.getenv("SESSION_DURATION", '0'))

    def create_session(self, user_id=None):
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        value = {
            'user_id':  user_id,
            'created_at': datetime.datetime.now()
        }
        self.user_id_by_session_id[session_id] = value
        return session_id

    def user_id_for_session_id(self, session_id=None):
        if not session_id:
            return None

        value = self.user_id_by_session_id.get(session_id)
        if not self.user_id_by_session_id[session_id]:
            return None
        if self.session_duration <= 0:
            return value['user_id']
        if not value['created_at']:
            return None

        created_at = value.get('created_at')
        session_age = datetime.datetime.now() - created_at

        if session_age > datetime.timedelta(seconds=self.session_duration):
            return None

        return value.get('user_id')
