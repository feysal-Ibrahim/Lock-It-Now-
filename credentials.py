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
              create method to save credential
                '''
