import unittest  # Importing the unittest module
from credentials import Credential # Importing the credential class
class TestCredential  (unittest.TestCase): # create a subclass  called TestUser, that inherits from unittest TestCase
    def setUp(self):
        self.new_user = Credential("facebook", "673766")  # create user object

    def tearDown(self):
     Credential.credentials_list = []

    def test_init(self):
        self.assertEqual(self.new_credentials.account_name, "acebook")
        self.assertEqual(self.new_credentials.password, "673766")

    def test_save_credentials(self):
          self.new_credentials.save_credentials()  # saving the new credentials
          self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credential("twitter", "123456")
        test_credentials.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 2)
        '''
    add another test case test_save_multiple_user to test if we can save multiple credentials in our credentials list.
        '''


    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test", "user", "0712345678", "test@user.com")  # new contact
            test_contact.save_contact()

            self.new_contact.delete_contact()  # Deleting a contact object
            self.assertEqual(len(Contact.contact_list), 1)