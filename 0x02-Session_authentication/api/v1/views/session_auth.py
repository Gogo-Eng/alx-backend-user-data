#!/usr/bin/env python3

"""Route module for the Session authentication
"""
from api.v1.views import app_views  # type: ignore
from typing import Tuple
from flask import Flask, jsonify, request
from models.user import User  # type: ignore
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """ POST /api/v1/auth_session/login
    Return:
      - the attributes of the user object
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or len(email.strip()) == 0:
        return jsonify({"error": "email missing"}), 400

    if password is None or len(password.strip()) == 0:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})

    if not user or len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    try:
        from api.v1.app import auth   # type: ignore
        session_id = auth.create_session(user[0].id)
    except AttributeError:
        raise AttributeError("The 'id' attribute is missing from the user.")

    response = jsonify(user[0].to_json())
    response.set_cookie(os.getenv("SESSION_NAME"), session_id)

    return response
