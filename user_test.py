import unittest  # Importing the unittest module
from user import User  # Importing the contact class
class TestUser  (unittest.TestCase): # create a subclass class called TestUser, that inherits from unittest TestCase
    def setUp(self):
        self.new_user = User("feysal", "ibrahim", "123456789")  # create user object
        User.user_list = []

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "feysal")
        self.assertEqual(self.new_user.last_name, "ibrahim")
        self.assertEqual(self.new_user.password, "123456789")
#
if __name__ == '__main__':
    unittest.main()