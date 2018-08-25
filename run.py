
#!/usr/bin/env python3.6#!/usr
from user import User

def create_user(fname, password):
    '''
    Function to create a new contact
    '''
    new_user = User(fname, password)
    return new_user
