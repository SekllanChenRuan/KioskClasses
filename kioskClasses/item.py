class Item():
    def __init__(self, itemid, weight, itemname, itemtype):
        self.itemid=itemid
        self.itemweight=weight
        self.itemname=itemname
        self.itemtype=itemtype

    def getItemid(self):
        return self.itemid

    def getItemname(self):
        return self.itemname

    def setItemname(self, itemname):
        return self.itemname=itemname
    
    def getItemtype(self):
        return self.itemtype

    def setItemtype(self, itemtype):
        return self.itemtype=itemtype

    def getItemweight(self):
        return self.itemweight
    
    def setItemweight(self, itemweight):
        return self.itemweight=itemweight

    def __str__(self):
        return self.itemid + ' ' self.itemname + ' ' self.itemtype + ' ' + self.itemweight
