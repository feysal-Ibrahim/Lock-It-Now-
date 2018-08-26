import random


class Credential:
     '''
        Will generate new instances of account credentials
        '''
     credential_list:[]

     def __init__(self, account_name, password):
          '''
           Passed in three arguments of the isntances of our variables
           '''
          self.account_name = account_name
          self.password = password

