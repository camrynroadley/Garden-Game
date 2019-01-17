#A standard trap

import pygame, constants

from block import *
from art import *

class Trap(Block):
 
    def __init__(self, x, y):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        self.art = Art()
        
        # Call the parent class (Block) constructor
        super().__init__(self.art.get_image('cardboard'), 40, 40)
 
        self.rect.x = x
        self.rect.y = y

        self.cost = 5

        #This is a feature that allows for timed removal of the trap.
        self.time = pygame.time.get_ticks()

        
        
    #Automatically removes the traps after 30 seconds
    def remove(self):
        time_alive = pygame.time.get_ticks()
        
        if time_alive - self.time > 30000:
            return False
        else:
            return True

    def get_x_coord(self):
        return self.rect.x
        
    def get_y_coord(self):
        return self.rect.y
