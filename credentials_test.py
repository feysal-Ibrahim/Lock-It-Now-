import unittest  # Importing the unittest module
from credentials import Credential # Importing the credential class
class TestCredential  (unittest.TestCase): # create a subclass  called TestUser, that inherits from unittest TestCase
    def setUp(self):
        self.new_user = Credential("facebook", "673766")  # create credentials object

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
    add another test case test_save_multiple_credentials to test if we can save multiple credentials in our credentials list.
        '''


    def test_delete_credntials(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credential("twitter",  "123456")  # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_contact()  # Deleting a credentials object
            self.assertEqual(len(Credential.credentials_list), 1)

    def test_display_all_credentials(self):
            self.assertEqual(Credential.display_credentials(), Credential.credentials_list)


if __name__ == '__main__':
    unittest.main()
