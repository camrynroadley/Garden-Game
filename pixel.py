#Pixel class used to help determine what grid square the player is on

import pygame, constants

from block import *

class Pixel(Block):

    def __init__(self):

        super().__init__(pygame.image.load('images/playerpixel.png'), 1, 1)

        self.rect.x = constants.SCREEN_WIDTH/2 + 20
        self.rect.y = constants.SCREEN_HEIGHT - 300 + 20
        self.x_speed = 0
        self.y_speed = 0

    def move_left(self):
        self.x_speed = -5 
    def move_right(self):
        self.x_speed = 5      
    def move_up(self):
        self.y_speed = -5       
    def move_down(self):
        self.y_speed = 5
    def stop_x(self):
        self.x_speed = 0
    def stop_y(self):
        self.y_speed = 0

    def update_position(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        #wrap to the opposite side to avoid going off screen
        if self.rect.x < 0:
            self.rect.x = constants.SCREEN_WIDTH
        if self.rect.x > constants.SCREEN_WIDTH:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = constants.SCREEN_HEIGHT
        if self.rect.y > constants.SCREEN_HEIGHT:
            self.rect.y = 0
