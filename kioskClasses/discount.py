class Discount():
    def __init__(self, discountid, discounttype, discountpercent):
        self.discountid=discountid
        self.discounttype=discounttype
        self.discountpercent=discountpercent
    
    def getDiscountid(self):
        return self.discountid

    def getDiscounttype(self):
        return self.discounttype

    def setDiscounttype(self, discounttype):
        return self.discounttype=discounttype

    def getDiscountpercent(self):
        return self.discountpercent

    def __str__(self):
        return self.discountid + ' ' self.discounttype + ' ' + self.discountpercent