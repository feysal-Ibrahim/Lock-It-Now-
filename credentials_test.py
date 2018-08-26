import unittest  # Importing the unittest module
from credentials import Credential # Importing the credential class
class TestCredential  (unittest.TestCase): # create a subclass  called TestUser, that inherits from unittest TestCase
    def setUp(self):
        self.new_credentials = Credential("facebook", "673766")  # create credentials object
        Credential.credentials_list = []

    def test_init(self):
         self.assertEqual(self.new_credentials.account_name, "facebook")
         self.assertEqual(self.new_credentials.password, "673766")

    def test_save_credentials(self):
      self.new_credentials.save_credentials()  # saving the new user
      self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credential("Twitter",  "987456")
        test_credentials.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 2)

        '''
     another test case test_save_multiple_user to test if we can save multiple user in our users list.
        '''

    def test_delete_credentials(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credential("Twitter", "987456")  # new contact
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()  # Deleting a contact object
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_display_all_credentials(self):
         self.assertEqual(Credential.display_credentials(), Credential.credentials_list)


if __name__ == '__main__':
    unittest.main()
