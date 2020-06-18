import unittest
from kiosk import Kiosk
from customer import Customer

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
        
