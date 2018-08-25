class User:
    """
       Class that generates new instances of users
       """
    users_list = []

    #Init method down here

    def __init__(self, first_name, password):
        """
              __init__ method helps us define our object
              Args:
                  user_name: New user name.
                  password: New user password.
              """

        self.first_name = first_name
        self.password = password
        """
             attribute for object.
            """

    def save_user(self):
       User.users_list.append(self)
       '''
     method to check is a user exists
        '''
    @classmethod
    def user_exists(cls, user_name):
     for user in cls.users_list:
        if user_name == user_name:
         return True
         return False