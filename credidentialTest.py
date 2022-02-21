import unittest
from credidentials import Credidential

class TestCredentials(unittest.TestCase):   
    """
    A test class that defines test cases for credentials class
    """ 
    def setUp(self):
        '''
        Method that runs before each individual credentials test methods run.
        '''
        self.my_cred = Credidential('facebook','silvano36','I34306488')

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credidential.credList = []

    def test_details(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        
        self.assertEqual(self.my_cred.accountType,'facebook')
        self.assertEqual(self.my_cred.username,'silvano36')
        self.assertEqual(self.my_cred.password,'I34306488') 

   
if __name__ == '__main__':
        unittest.main()