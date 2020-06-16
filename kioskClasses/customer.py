from user import User

#This is my attempt in inheriting from User
class Customer(User):
    def __init__(self, customerid):
        User.__init__(userid, firstname, lastname, phonenumber)
        self.customerid=customerid
        self.userid=userid
        self.firstname=firstname
        self.lastname=lastname
        self.phonenumber=phonenumber

    def getCustomerid(self):
        return self.customerid

    def getCustomername(self):
        return self.customername=self.firstname + ' ' + self.lastname 

    def __str__(self):
        return  self.customerid + ' ' self.customername

#used w3schools code for reference

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.welcome()