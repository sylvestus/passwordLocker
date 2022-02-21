
import string
import random


class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    userList = []
    def addUser(self):
        '''
        method saves a new user object to credentials list
        '''
        User.userList.append(self)

    def deleteUser(self):
       '''
        method deletes a saved user from user_list
        '''   
       User.userList.remove(self)
       
    @classmethod
    def displayUser(cls):
        return cls.userList

    def generate_password(self):
        '''
        generate random password consisting of letters
        '''
        password = string.ascii_uppercase + string.ascii_lowercase
        return ''.join(random.choice(password) for i in range(1,9))

    

       



        