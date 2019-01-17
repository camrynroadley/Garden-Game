"""
Base block class for our sprites.
"""


import pygame

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, image, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = image
        
        
        self.rect = self.image.get_rect()
