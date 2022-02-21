from user import User


class Credidential:
    def __init__(self,accountType,username,password):
        self.accountType = accountType
        self.username = username
        self.password = password
    
    credList = []
    def addCred(self):
        Credidential.credList.append(self)
    
    