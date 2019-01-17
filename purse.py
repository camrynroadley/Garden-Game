'''
Purse class
Contains functions for player currency
'''

class Purse:
    def __init__(self):
        self.money = 0

    def canBuy(self, purchaseAmount):
        if(self.money - purchaseAmount >= 0):
            return True
        else:
            return False

    def buy(self, purchaseAmount):
        if(self.canBuy(purchaseAmount)):
            self.money -= purchaseAmount

    def sell(self, profit):
        self.money+= profit
