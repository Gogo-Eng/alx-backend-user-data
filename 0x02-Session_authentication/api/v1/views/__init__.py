#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint # type: ignore
from models.user import User # type: ignore gogo

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import * # type: ignore
from api.v1.views.users import * # type: ignore

User.load_from_file()
