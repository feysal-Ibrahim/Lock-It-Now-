class User:
    """
       Class that generates new instances of users
       """
    users_list = []

    #Init method down here

    def __init__(self, user_name, password):
        """
              __init__ method helps us define our object
              Args:
                  user_name: New user name.
                  password: New user password.
              """

        self.user_name = user_name
        self.password = password
        """
            create attribute for object.
            """

    def save_user(self):
       User.users_list.append(self)
       '''
      create method to check is a user exists
        '''

    @classmethod
    def user_login(cls, user_name):
           '''
           Method that finds a user and logs them in
           '''
           for user in cls.users_list:
               if user.name == user_name:
                   return user


    @classmethod
    def user_exists(cls, user_name):
        for user in cls.users_list:
         if user_name == user_name:
            return True

    @classmethod
    def generate_password(cls, pass_length):
        '''
        class to generate passowrds
        '''
        allchar = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(random.sample(allchar, int(pass_length)))
        return password