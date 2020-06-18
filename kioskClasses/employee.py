# from user import User

#This is my attempt in inheriting from User
class Employee():
    def __init__(self, employeeid, employeeposition, hiredate, firstname, lastname):
        # User.__init__(userid, firstname, lastname, phonenumber)
        self.employeeid=employeeid
        self.employeeposition=employeeposition
        self.hiredate=hiredate
        self.employeename=firstname + ' ' + lastname


    def getEmployeename(self):
        return self.employeename
        

    def getEmployeeid(self):
        return self.employeeid

    def getEmployeeposition(self):
        return self.employeeposition
    
    def setEmployeeposition(self, employeeposition):
        self.employeeposition=employeeposition

    def setEmployeephonenumber(self, phonenumber):
        self.phonenumber=phonenumber

    def getHiredate(self):
        return self.hiredate
    
    def __str__(self):
        return self.employeeid + ' ' + self.employeename + ' ' + self.employeeposition + ' ' + self.hiredate


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