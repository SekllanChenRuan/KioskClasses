class Kiosk():
    def __init__(self, kioskid, kiosknumber):
        self.kioskid=kioskid
        self.kiosknumber=kiosknumber
        # self.status is: referring to if a kiosk is available to service customers or not
        self.status='available'
        
    def getKioskid(self):
        return self.kioskid

    def getKiosknumber(self):
        return self.kiosknumber
    
    # I think it's a good idea to be able to to set the kiosk number as an easier identifier for humans
    def setKiosknumber(self, kiosknumber):
        self.kiosknumber=kiosknumber

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status=status

    def __str__(self):
        return self.kioskid + ' ' + self.kiosknumber + ' ' + self.status



