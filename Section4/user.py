# June 9th

# this file creates user object, so we no longer need dictionaries containing user info

class User:
    def __init__(self, _id, username, password):
        self.id = _id      # we use _id instead of id because id is a python keyword
        self.username = username
        self.password = password

