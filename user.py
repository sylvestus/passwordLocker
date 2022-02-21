
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

   