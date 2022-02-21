from user import User


class Credidential:
    def __init__(self,accountType,username,password):
        self.accountType = accountType
        self.username = username
        self.password = password
    
    credList = []
    def addCred(self):
        Credidential.credList.append(self)
    
    def deleteCred(self):
        Credidential.deleteCred.remove(self)
    
    @classmethod
    def displaycred(cls):
        return cls.credList

    @classmethod
    def verify(cls,username,password):
        accountUser =""
        for user in User.userList:
            if User.username == username and User.password == password:
                accountUser = username
                return accountUser
    
    @classmethod
    def findcred(cls,accountType):
        for credidential in cls.credList:
            if credidential.accountType == accountType:
                return credidential
