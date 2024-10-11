#!/usr/bin/env python3

import bcrypt

"""
Hashing and verifying passwords
"""


def _hash_password(password: str) -> bytes:
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password
