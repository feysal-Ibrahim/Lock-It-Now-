#!/usr/bin/env python3.6
from user import User
from credentials import Credential



def create_user_credentials(user_name, password):
    '''
    creates a new user
    '''
    new_user = User(user_name, password)
    return new_user


def save_user(user):
    '''
    will save new_users
    '''
    user.save_user()

def user_login(user_name):
    '''
        Function to login users
        '''
    return User.user_login (user_name)


def user_exists(user_name):
    '''
    will search for user using user_name
    '''
    return User.user_exists(user_name)


def create_credentials(account_name, password):
    """
        Function to save new_profile
        """
    new_credentials = Credential(account_name, password)
    return new_credentials


def save_credentials(credentials):
    """
        Function save a user credentials
        """
    credentials.save_credentials()


def delete_credentials(credentials):
    """
    delete a credential
    """
    Credential.delete_credentials()

def find_credentials(account_name):
  '''
	Function that finds an account using th ephone number and returns the account
	'''
  return Credential.find_credentials(account_name)


def check_if_credentials_exists(account_name):
   '''
 	Function that checks if an account exists
    '''
   return Credential.credentials_exist(account_name)




def check_if_user_exists(user_name):
    '''
     Function that checks if a user exists
       '''
    return User.user_exist(user_name)


def display_credential():
    '''
     Function that returns all the saved contacts
    '''
    return Credential.display_credentials ()


def generate_password(pass_length):
    '''
	Function that generates a password
	'''
    return Credential.generate_password (pass_length)

def main():
    print("I AM LOCKING YOUR PASSWORD NOW! ITS NOT A RUDE WAY, JUST FOR YOUR SAFETY")
    print("enter your name!")
    user_name = input()
    print("enter password")
    password = input()
    save_user(create_user_credentials(user_name, password))
    print(f"""Your user details - Username : {user_name}  Password : {password}""")

    while True:
       print("Use these short codes: cnc - create new credentials, dc - display credentials, fc - find a credential, exit - exit credentials list")
       short_code = input().lower()

       if short_code == 'cnc':
           print ("enter new account name")
           account_name=input()
           print("set password")
           password = input()
           print ("besides the password you generated now, WE would also like to generate password for you incase! How long would you like your password to be")
           pass_length = int(input())
           password = generate_password(pass_length)
           save_credentials (create_credentials(account_name, password, ))

           print (f"New credentials detail : Credential: {account_name}, Password: {password}", )




       elif short_code == 'dc':
           if display_credential():
               print ("Below is a list of all your accounts")
               for Credential in display_credential():
                   print (f"Credential : {Credential.account_name}, Password : {Credential.password}")

                   print ('')
           else:
               print("DATABASE ERROR! it seems you havent saved your credentials yet, Try saving by using the SHORT CODES above!")


       elif short_code == 'fc':
            print("enter  the account name for the password ")
            account_input = input()
            if check_if_credentials_exists(account_input):
                account_input = find_credentials(account_input)
                print(f"{account_input.account_name}, {account_input.password}")
                print('')
            else:
                print("DATABASE ERROR!(404 file not found)account does not exist")
       elif short_code == 'exit':
           print("WHY!  THE MACHINE HATES YOU GOING!!, its okey if you decide but DO COME AGAIN!")
           print ('')
           break
       else:
           print("404 error, (Inputs not found) Kindly try using the short code provided for consistency")
           print ('')






if __name__ =='__main__':
    main()

