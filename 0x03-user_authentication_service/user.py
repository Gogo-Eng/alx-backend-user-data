#!/usr/bin/env python3
"""creating a SQLAlchemy model named User for a database table
"""

from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """User model"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    session_id = Column(String(255), nullable=True)
    reset_token = Column(String(255), nullable=True)
