import unittest
from kiosk import Kiosk
from customer import Customer
from employee import Employee

class KioskTest(unittest.TestCase):
    def setUp(self):
        self.kiosk=Kiosk('2526', '1')

    def test_kioskstring(self):
        self.assertEqual(str(self.kiosk),'2526 1 available')

    def test_getKioskId(self):
        self.assertEqual(self.kiosk.getKioskid(), '2526')
    
    def test_getKioskNumber(self):
        self.assertEqual(self.kiosk.getKiosknumber(), '1')

    def test_setKioskNumber(self):
        self.kiosk.setKiosknumber('2')
        self.assertEqual(self.kiosk.getKiosknumber(), '2')

    def test_getStatus(self):
        self.assertEqual(self.kiosk.getStatus(), 'available')

    def test_setStatus(self):
        self.kiosk.setStatus('unavailable')
        self.assertEqual(self.kiosk.getStatus(), 'unavailable')


class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer=Customer('1234', 'Abra', 'Cadabra')

    def test_CustomerString(self):
        self.assertEqual(str(self.customer), '1234 Abra Cadabra')
    
    def test_getCustomerId(self):
        self.assertEqual(self.customer.getCustomerid(), '1234')

    def test_getCustomerName(self):
        self.assertEqual(self.customer.getCustomername(), 'Abra Cadabra')
        
class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee=Employee('23','Associate','today','1233','Keith','Leon','1233456789')
    
    def test_EmployeeString(self):
        self.assertEqual(str(self.employee), '23 Keith Leon Associate today')
    
    def test_getEmployeeName(self):
        self.assertEqual(self.employee.getEmployeename(), 'Keith Leon')

    def test_getEmployeeId(self):
        self.assertEqual(self.employee.getEmployeeid(), '23')
    
    def test_getEmployeePosition(self):
        self.assertEqual(self.employee.getEmployeeposition(), 'Associate')

    def test_getHireDate(self):
        self.assertEqual(self.employee.getHiredate(), 'today')

    def test_setEmployeePosition(self):
        self.employee.setEmployeeposition('Manager')
        self.assertEqual(self.employee.getEmployeeposition(), 'Manager')
    
    def test_setEmployeePhonenumber(self):
        self.employee.setEmployeephonenumber('1233331111')
        self.assertEqual(self.employee.getPhonenumber(), '1233331111')

