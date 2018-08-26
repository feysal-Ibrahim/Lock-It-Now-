import unittest  # Importing the unittest module
from credentials import Credential # Importing the credential class
class TestCredential  (unittest.TestCase): # create a subclass  called TestUser, that inherits from unittest TestCase
    def setUp(self):
        self.new_user = Credential("facebook", "673766")  # create user object
        Credential.credentials_list = []

    def test_init(self):
         self.assertEqual(self.new_credentials.account_name, "feysal")
         self.assertEqual(self.new_credentials.password, "123456789")

    def test_save_user(self):
             self.new_credentials.save_credentials()  # saving the new credentials
             self.assertEqual(len(Credential.credentials_list), 1)