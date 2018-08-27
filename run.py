#!/usr/bin/env python3.6
from user import User
from credentials import Credential
import random
import string

def create_user(first_name, password):
    '''
    creates a new user
    '''
    new_user = User(first_name, password)
    return new_user

def save_user(user):
    '''
    will save new_users
    '''
    user.save_user()

def user_exists(first_name):
    '''
    will search for user using user_name
    '''
    return User.user_exists(first_name)

def create_credentials(account_name, password):
        """
        Function to save new_profile
        """
        new_profile = Credential(account_name, password)
        return new_profile

def save_credentials(credentials):
        """
        Will save a user credentials
        """
        credentials.save_credentials

def password_generator():
            """
            A function that generates a random password
            """
            chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
            size = random.randint(6, 20)
            password = "".join(random.choice(chars) for character in range(size))

            return password

def display_credentials():
    """
    Function to use credentials
    """
    return Credential.display_credentials()

def delete_credentials(credentials):
    """
    delete a credential
    """
    Credential.delete_credentials()

def main():
        print("Hello! Welcome to Password Locker. What is your name?")
        name = input()

        print(f"Hi {name}, Type new to create a new password locker account")

        while True:
            short_code = input().lower()
            if short_code == "new":
                print('__' * 25)
                print("New Password Locker Account")
                print("\n")
                print("Enter a preferred first name")
                first_name = input()

                print("We can generate a password for you or you can set it by yourself")
                print("""Use these short codes:
                           gen-To generate a password
                           make-To make a password on your own""")
                code = input().lower()
                print("\n")
                if code == "make":
                    print("write a password of your own")
                    password = input()
                elif code == "gen":
                    password = password_generator()
                    print(f"Your password is {password}")
                    break
                else:
                    print("Please type make or gen")
                    break
                save_user(create_user(first_name, password))
                break

print(f"User-{user_name}, password-{password}")
print("You successfully created your new account")
print("__" * 25)

print("You can now create and view password locker accounts")
while True:
    print("""Type one of these short codes:
                      np - create password credentials
                      dp - display password locker credentials
                      """)
    short_codes = input().lower()
    if short_codes == "np":
        print("""Type in one of the short_codes,
                       write - make a password so that we can store it for you,
                       generate - we will randomize a password for you
                       """)
        sec_code = input().lower()

        if sec_code == "write":
            print("Enter a name of the account you wish to create")
            account_name = input()
            print("Enter a password for the account")
            security_code = input()

        elif sec_code == "generate":
            print("Enter a name of the account you wish to create")
            account_name = input()
            security_code = password_generator()
            print(f"We have stored your credentials as account name - {account_name} and password - {security_code}")

        else:
            print("Use one of the short codes")
        save_credentials(create_credentials(account_name, password))
        break
        print("You successfully created and stored your credentials")
        print("__" * 25)

    elif short_codes == "dp":
        print("Enter an account name to search for credentials")
        view = input().lower()
        if view == account_name:
            for credentials in display_credentials():
                print(f"{account_name}, {security_code}")

            else:
                print("The account not exist")
                break

        else:
            print("Use one of the short codes as instructed")
            break

print("__" * 25)
print("Thank you for visiting Password Locker. Come again. Ciao!")

if __name__ == '__main__':
    main()







