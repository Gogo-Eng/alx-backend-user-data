#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

user1 = my_db.add_user("test@test.com", "PwdHashed")
print(f"The id attached to {user1.email}, is {user1.id}")
user2 = my_db.add_user("progressgogochinda@gmail.com", "sword")
print(f"The id attached to {user2.email}, is {user2.id}")

find_user1 = my_db.find_user_by(email="test@test.com")
print(find_user1.id)
find_user2 = my_db.find_user_by(email="progressgogochinda@gmail.com", hashed_password="sword")
print(find_user2.id)
try:
    find_user2 = my_db.find_user_by(email="progressgogochinda@gmail.com", hashed_password="sword")
    print(find_user2.id)
    find_user = my_db.find_user_by(email="test7@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")        
