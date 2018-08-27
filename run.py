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
    new_credentials = Credential (account_name, password)
    return new_credentials


def save_credentials(credentials):
    """
        Function save a user credentials
        """
    credentials.save_credentials


def delete_credentials(credentials):
    """
    delete a credential
    """
    Credential.delete_credentials()

def find_credentials(password):
	'''
	Function that finds an account using th ephone number and returns the account
	'''
	return Credential.find_by_password(password)


def check_if_credentials_exists(password):
    '''
	Function that checks if an account exists
	 '''
    return Credential.credentials_exist (password)




def check_if_user_exists(user_name):
    '''
     Function that checks if a user exists
       '''
    return User.user_exist(user_name)


def display_credentials():
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
    print ("Welcome to password locker")
    while True:
        print('''
                     ca - create account
                     lg - login
                     esc - Escape''')
        short_code = input ().lower ()
        print ("_" * 20)
        if short_code == "ca":
            print ('''Create your Credential mahn!!
            Enter your full name
                                 ''')
            print ("_" * 20)
            user_name = input ()

            print ("Enter Your Password")
            password =input()
            save_user(create_user_credentials(user_name, password))
            print ("_" * 20)
            print ("_" * 20)
            print (f"""Your user details - Username : {user_name}  Password : {password}""")
            print("_" * 20)
            print("_" * 20)

            print ("")
            print (f"Hi {user_name} What would you like to do?")
            print ("")

            while True:
                print (
                    "Use these short codes: cnc - create new credentials, dc - display credentials, fc - find a credential, exit - exit credentials list")
                short_code = input ().lower ()

                if short_code == 'cnc':
                    print ("Creating a New Credential")
                    print ("-" * 10)

                    print ('')

                print ("Credential name ...")
                account_name = input()

                print ('')

                print("password ...")
                password = input()

                print('')

                print ("besides the password you generated now, WE would also like to generate password for you incase! How long would you like your password to be")
                pass_length = int (input ())
                password = generate_password (pass_length)

                save_credentials(create_credentials (account_name,  password, ))
                print ('')

                print (
                    f"New credentials detail : Credential: {account_name}, Password: {password}", )
                print('')

        elif short_code == 'dc':
                if display_credentials():
                    print ("Below is a list of all your accounts")
                print ("-" * 20)

        print('')
        for Credential in display_credentials():
            print(f"Credential : {Credential.account_name}, Password : {Credential.password}")

            print('')
        else:
            print ('')
            print ("You seem to not have any saved accounts yet. Save an account using the cc code")
            print ('')

        # elif  short_code== "lg":
        #  print("Log in")
        print("user_name")
        print("_" * 20)
        user_name = input ( )
        print ("Enter Your Password")
        password = input()
        if check_if_user_exists(user_name):
            authenticate_user = user_login(user_name)
            if authenticate_user.user_name == user_name and authenticate_user.password == password:
                print("")



                while True:
                    print("Use these short codes: cac - create new account, dac - display account, fac - find an account, exit - exit accounts list")
                    short_code = input().lower()

                    if short_code == 'cac':
                        print("Creating a New Credential")
                        print("-" * 10)

                        print ('')

                        print("Credential name ...")
                        account_name = input()

                        print('')

                        print ("User name ...")
                        user_name = input ( )

                        print('')

                        print("User name ...")

                        print('')

                        print ("How long would you like your password to be")
                        pass_length = int (input())
                        password = generate_password(pass_length)

                        save_credentials(create_credentials(account_name,  user_name,  password))
                        print('')

                        print("Your New account details including your auto generated password are shown below")
                        print('')

                        print(f"New account details : Account: {account_name},Email:{email}, Password: {password}",)
                        print('')
        #
        # elif short_code == "exit":
        #      print('')
        #      print("Goodbye ...")
        #      break
        #
        #
        # else:
        #        print("Please input a valid short code")
        #
        #
        # else:
        #   print ("A user with that username does not exist. Please register to start using the application")
   # elif short_code == "esc"
   #   print('')
   #   print("Exiting")
   #   break else:
   #   print ("I'm sorry, the short code does not seem to exist")

if __name__ == '__main__':
        main ()



