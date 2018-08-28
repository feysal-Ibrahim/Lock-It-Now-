import unittest  # Importing the unittest module
from credentials import Credential  # Importing the credential class
class TestCredential  (unittest.TestCase): # create a subclass  called TestUser, that inherits from unittest TestCase
    def setUp(self):
        self.new_credentials = Credential("facebook", "673766")  # create credentials object

    def tearDown(self):
        Credential.credentials_list = []

    def test_init(self):
         self.assertEqual(self.new_credentials.account_name, "facebook")
         self.assertEqual(self.new_credentials.password, "673766")

    def test_save_credentials(self):
      self.new_credentials.save_credentials()  # saving the new user
      self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_credentials(self):
          '''
          test_save_multiple_accounts to check if we can save multiple accounts
              objects to our account_list
          '''
          self.new_credentials.save_credentials()
          test_credentials = Credential("github", "987123")
          test_credentials.save_credentials()
          self.assertEqual(len(Credential.credentials_list), 2)



    def test_delete_credentials(self):
        '''
        test_delete_account to test if an account can be deleted from the account_list
        '''
        self.new_credentials.save_credentials()
        Credential("github", "987123").save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_display_all_credentials(self):
            '''
            method that returns all contacts saved
            '''
            self.assertEqual(Credential.display_credentials(), Credential .credentials_list)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credential("github", "987123")  # new contact
        test_credentials.save_credentials()

        credentials_exists = Credential.credentials_exist("987123")
        self.assertTrue(credentials_exists)

if __name__ == '__main__':
    unittest.main()
