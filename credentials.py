import random

class Credential:
     '''
        Will generate new instances of account credentials
        '''
     credentials_list:[]

     def __init__(self, account_name, password):
          '''
           Passed in three arguments of the isntances of our variables
           '''
          self.account_name = account_name
          self.password = password
          """
            create attribute for object.
            """

     def save_user(self):
        Credential.credentials_list.append(self)
        '''
        saving credentials object into object list
        '''
     def delete_credentials(self):
         Credential.credentials_list.remove(self)


@classmethod
def display_credentials(cls, user_name):
    """
    this method will take a user_name and
    return credentials that matches that user_name
    """
    for credentials in cls.credentials_list:
            if credentials.user_name == user_name:
               return credentials