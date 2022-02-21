import unittest  # Importing the unittest module
from user import User  # Importing the contact class


class Testuser(unittest.TestCase):

    def setUp(self):
        """
        a method that runs before the test
        """
        self.new_user = User('silvano', 'I34306488')

    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """

        self.assertEqual(self.new_user.username, 'silvano')
        self.assertEqual(self.new_user.password, 'I34306488')

    def test_addUser(self):
        '''
        check if the new instance of the user object has been created
        '''
        
        self.new_user.addUser()
        self.assertEqual(len(User.userList),1)

if __name__ == '__main__':
        unittest.main()