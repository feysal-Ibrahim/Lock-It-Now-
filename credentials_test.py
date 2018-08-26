import unittest  # Importing the unittest module
from credentials import Credential # Importing the credential class
class TestCredential  (unittest.TestCase): # create a subclass  called TestUser, that inherits from unittest TestCase
    def setUp(self):
        self.new_user = Credential("facebook", "673766")  # create user object
        Credential.credential_list = []

    def test_init(self):
         self.assertEqual(self.new_user.first_name, "feysal")
         self.assertEqual(self.new_user.password, "123456789")