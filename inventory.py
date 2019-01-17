#Inventory class to keep track of all items. Uses TrapBag and SeedBag
#Inventory is basically a funnel to keep the other item categories in one place


from seedBag import *
from trapBag import *
from purse import*


class Inventory:
    def __init__(self):
        self.trapBag = TrapBag()
        self.seedBag = SeedBag()
        self.purse = Purse()

    
