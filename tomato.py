import pygame, constants

from block import *
from art import *

class Tomato(Block):
 
    def __init__(self, x, y):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """

        self.art = Art()
        
        # Call the parent class (Block) constructor
        super().__init__(self.art.get_image('tomato1'), 40, 40)
 
        self.rect.x = x
        self.rect.y = y

        self.time = pygame.time.get_ticks()

        self.eatable = False
        self.harvestable = False

        self.cost = 4
        self.sell_value = 7

        
    #Plants grow in three phases- seeded, growing, fully grown
    #Plant grows over time
    def grow(self):
        time_alive = pygame.time.get_ticks()
        #Still growing, becomes eatable
        if (time_alive - self.time) > 20000:
            self.image = self.art.get_image('tomato2')
            self.eatable = True
        #Fully grown, becomes harvestable
        if time_alive - self.time > 35000:
            self.image = self.art.get_image('tomato3')
            self.harvestable = True

    def get_x_coord(self):
        return self.rect.x
        
    def get_y_coord(self):
        return self.rect.y
