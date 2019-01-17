#Controls the number of seeds the player owns

class SeedBag:
    def __init__(self):
        #Initialize with (currently) five seeds of each type
        self.numOfCarrotSeeds = 5
        self.numOfCabbageSeeds = 5
        self.numOfPepperSeeds = 5
        self.numOfTomatoSeeds = 5

    #Plants a carrot
    def plantCarrotSeed(self):
        self.numOfCarrotSeeds -= 1

    #Determines if a carrot seed can be planted
    def canPlantCarrotSeed(self):
        if(self.numOfCarrotSeeds != 0):
            return True
        else:
            return False

    #Plants a cabbage
    def plantCabbageSeed(self):
        self.numOfCabbageSeeds -= 1

    #Determines if a cabbage seed can be planted
    def canPlantCabbageSeed(self):
        if(self.numOfCabbageSeeds > 0):
            return True
        else:
            return False

    #Plants a pepper
    def plantPepperSeed(self):
        self.numOfPepperSeeds -= 1
    #Determines if a pepper can be planted
    def canPlantPepperSeed(self):
        if(self.numOfPepperSeeds > 0):
            return True
        else:
            return False

    #Plants a tomato
    def plantTomatoSeed(self):
        self.numOfTomatoSeeds -= 1
    #Determines if a tomato can be planted
    def canPlantTomatoSeed(self):
        if(self.numOfTomatoSeeds > 0):
            return True
        else:
            return False
