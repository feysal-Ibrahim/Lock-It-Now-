import string
import random


class Credential:
    '''
        Will generate new instances of account credentials
        '''
    credentials_list = []

    def __init__(self, account_name, password):
        '''
           Passed in three arguments of the isntances of our variables
           '''
        self.account_name = account_name
        self.password = password
        """
            create attribute for object.
            """

    def save_credentials(self):
        Credential.credentials_list.append (self)
        '''
        saving credentials object into object list
        '''

    def delete_credentials(self):
        Credential.credentials_list.remove (self)

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def find_credentials(cls, account_name):
        '''
       M ethod that checks if an account exists from the credentials list.

         '''
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials


    @classmethod
    def credentials_exist(cls, account_name):
        '''
       M ethod that checks if an account exists from the credentials list.

         '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return True
            return False

    @classmethod
    def generate_password(cls, pass_length):
        '''
        class to generate passowrds
        '''
        allchar = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(random.sample(allchar, int(pass_length)))
        return password
