#!/usr/bin/python3

from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

host = "localhost"
password = "Professional28#"
username = "root"
port = 3306
database = "DB"

url = f"mysql+mysqldb://{username}:{password}@{host}:{str(port)}/{database}"
engine = create_engine(url)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    session_id = Column(String(255), nullable=True)
    reset_token = Column(String(255), nullable=True)


Base.metadata.create_all(engine)
