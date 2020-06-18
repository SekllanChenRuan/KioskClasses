class User():
    def __init__(self, userid, firstname, lastname, phonenumber):
        self.userid=userid
        self.firstname=firstname
        self.lastname=lastname
        self.phonenumber=phonenumber

    def getUserid(self):
        return self.userid

    # I will not set userid because I think it should be auto generated

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname
    
    def getPhonenumber(self):
        return self.phonenumber

    def __str__(self):
        return self.userid + ' ' + self.firstname + ' ' + self.lastname + ' ' + self.phonenumber