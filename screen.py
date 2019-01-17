#Abstract class, making sure that all subclasses at least attempt
# to implement the update, draw, and handle_keyboard_event methods

import pygame
import constants

class Screen():
    def __init__(self):
        self._font = pygame.font.SysFont('Calibri', 15, True, False)
        self._hotbar_font = pygame.font.SysFont('castellar', 24, True, False)
        self._hotbar_plant_font = pygame.font.SysFont('castellar', 16, True, False)
        
    def handle_keyboard_event(self, event):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
        
    def draw(self, screen):
        raise NotImplementedError
