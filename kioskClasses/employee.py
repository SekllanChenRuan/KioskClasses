from user import User

#This is my attempt in inheriting from User
class Employee(User):
    def __init__(self, employeeid, employeeposition, hiredate, firstname, lastname, phonenumber):
        User.__init__(userid, firstname, lastname, phonenumber)
        self.employeeid=employeeid
        self.employeeposition=employeeposition
        self.hiredate=hiredate
        self.userid=userid
        self.firstname=firstname
        self.lastname=lastname
        self.phonenumber=phonenumber
    
    def getEmployeename(self):
        return self.employeename=self.firstname + ' ' self.lastname

    def getEmployeeid(self):
        return self.employeeid

    def getEmployeeposition(self):
        return self.employeeposition
    
    def setEmployeeposition(self, employeeposition):
        return self.employeeposition=employeeposition

    def setEmployeephonenumber(self, phonenumber):
        return self.phonenumber=phonenumber

    def getHiredate(self):
        return self.hiredate
    
    def __str__(self):
        return self.employeeid + ' ' + self.employeename + ' ' + self.employeeposition + ' ' self.hiredate


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