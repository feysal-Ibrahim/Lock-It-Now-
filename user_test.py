import unittest  # Importing the unittest module
from user import User  # Importing the user class
class TestUser  (unittest.TestCase): # create a subclass class called TestUser, that inherits from unittest TestCase
    def setUp(self):
        self.new_user = User("feysal", "123456789")  # create user object
    def tearDown(self):
        User.users_list = []
        '''
        saving users object into object list
        '''

    def test_init(self):
        
         self.assertEqual(self.new_user.user_name, "feysal")
         self.assertEqual(self.new_user.password, "123456789")

    '''
          test to confirm if user class object has been instantiated correctly
         '''

    def test_save_user(self):
      self.new_user.save_user()  # saving the new user
      self.assertEqual(len(User.users_list), 1)

      '''
          test_save accounts to check if we can save a user account
      '''


    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Waititu",  "0713027855")
        test_user.save_user()
        self.assertEqual(len(User.users_list), 2)

        '''
         test case test_save_multiple_user to test if we can save multiple user in our users list.
        '''

    def test_user_login(self):
            '''
            Test case to test user login
            '''
            self.new_user.save_user ()
            test_user = User ("Sonko", "58468")
            test_user.save_user ()

            find_user = User.user_name ("Sonko")
            self.assertEqual(find_user.user_name, test_user.user_name)

            '''
          test_save accounts to check if we  a user can log in to his/her account
              '''

    def test_user_exists(self):
        '''
              Method that checks if a user exists from the user list.
              Returns :
                  Boolean: True or false depending if the user exists
              '''

        self.new_user.save_user()
        test_user = User("Waititu", "0713027855")
        test_user.save_user()

        user_exists = User.user_exists("Waititu")

        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
