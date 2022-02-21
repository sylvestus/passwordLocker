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

    def test_addCred(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.my_cred.addCred()
        self.assertEqual(len(Credidential.credList),1)

    def test_save_multiple_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.my_cred.addCred()
        test_cred = Credidential('facebook','silvano36','I34306488')
        test_cred.addCred()
        self.assertEqual(len(Credidential.credList),2)

if __name__ == '__main__':
        unittest.main()