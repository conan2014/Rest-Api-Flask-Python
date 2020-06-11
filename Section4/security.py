# June 9th

from werkzeug.security import safe_str_cmp  # safe_str_cmp method is used to compare strings
from user import User

# This security file contains a few important functions

# The 1st thing is an in-memory table of all registered users

users = [
    User(1, 'bob', 'asdf')
]

# the 2nd thing are 2 mappings

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}

# Here is the 1st function to authenticate a user when a user gives us their username and password

def authenticate(username, password):
    user = username_mapping.get(username, None)  # we can directly retrieve user by username without iterating over a list
    if user and safe_str_cmp(user.password, password):
        return user


# Here is the identity function that is unique to Flask_JWT, it takes in payload parameter, which is the content of the JWT token

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)   # we can directly retrieve user by userid without iterating over a list










