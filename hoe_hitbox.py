'''
This invisible box represents the hoe's hit range
'''

import pygame, constants
from block import *

class HoeHitbox(pygame.sprite.Sprite):

    def __init__(self):

        #Call parent (sprite) constructor
        super().__init__()

        #create an image of the block and fill it with color
        self.image = pygame.Surface([30, 40])
        self.image.fill(constants.RED)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
