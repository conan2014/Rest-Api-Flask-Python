# June 9th

# This security file contains a few important functions

# The 1st thing is an in-memory table of all registered users

users = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]

# the 2nd thing are 2 mappings

username_mapping = {'bob': {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

userid_mapping = {1: {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

# Here is the 1st function to authenticate a user

def authenticate(username, password):
    user = username_mapping.get(username, None)  # we can directly retrieve user by username without iterating over a list
    if user and user.password == password:
        return user


# Here is the identity function that is unique to Flask_JWT, it takes in payload parameter, which is the content of the JWT token

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)   # we can directly retrieve user by userid without iterating over a list










