class Sale():
    def __init__(self, saleid, saletotal, saledate, salequantity)
        self.saleid=saleid
        self.saletotal=saletotal
        self.saledate=saledate
        self.salequantity=salequantity

    def getSaleid(self):
        return self.saleid

    def getSaletotal(self):
        return self.saletotal

    def getSaledate(self):
        return self.saledate

    def getSalequantity(self):
        return self.salequantity
    
    def __str__(self):
        return self.Saleid + ' ' + self.salequantity + ' ' + self.Saledate + ' ' + self.saletotal
