"""
Implements all art objects.
"""

import pygame
import title_screen
import game_screen
import constants
import block

from level_manager import *
from file_manager import *

class Art():

    # creates the art object
    def __init__(self):
        self._ground_tile = pygame.image.load(FileManager().get_path('ground'))
        self._plant_tile = pygame.image.load(FileManager().get_path('plantable'))
        self._bunny = pygame.image.load(FileManager().get_path('bunny'))
        self._bunny_run1 = pygame.image.load(FileManager().get_path('run1'))
        self._bunny_run2 = pygame.image.load(FileManager().get_path('run2'))
        self._bunny_run3 = pygame.image.load(FileManager().get_path('run3'))
        self._carrot1 = pygame.image.load(FileManager().get_path('carrot1'))
        self._carrot2 = pygame.image.load(FileManager().get_path('carrot2'))
        self._carrot3 = pygame.image.load(FileManager().get_path('carrot3'))
        self._cabbage1 = pygame.image.load(FileManager().get_path('cabbage1'))
        self._cabbage2 = pygame.image.load(FileManager().get_path('cabbage2'))
        self._cabbage3 = pygame.image.load(FileManager().get_path('cabbage3'))
        self._player = pygame.image.load(FileManager().get_path('player'))
        self._cardboard_trap = pygame.image.load(FileManager().get_path('cardboard'))
        self._pepper1 = pygame.image.load(FileManager().get_path('pepper1'))
        self._pepper2 = pygame.image.load(FileManager().get_path('pepper2'))
        self._pepper3 = pygame.image.load(FileManager().get_path('pepper3'))
        self._tomato1 = pygame.image.load(FileManager().get_path('tomato1'))
        self._tomato2 = pygame.image.load(FileManager().get_path('tomato2'))
        self._tomato3 = pygame.image.load(FileManager().get_path('tomato3'))
        self._dirt = pygame.image.load(FileManager().get_path('dirt'))
        self._grass = pygame.image.load(FileManager().get_path('grass'))
        self._pixel = pygame.image.load(FileManager().get_path('pixel'))
        self._marker = pygame.image.load(FileManager().get_path('marker'))
        self._shopTile = pygame.image.load(FileManager().get_path('shopTile'))
        self._shopBorderTile = pygame.image.load(FileManager().get_path('shopBorderTile'))


    # retrieves images initialized referenced by id
    def get_image(self, id):
        if id == 'ground':
            return self._ground_tile
        elif id == 'plantable':
            return self._plant_tile
        elif id == 'bunny':
            return self._bunny
        elif id == 'run1':
            return self._bunny_run1
        elif id == 'run2':
            return self._bunny_run2
        elif id == 'run3':
            return self._bunny_run3
        elif id == 'carrot1':
            return self._carrot1
        elif id == 'carrot2':
            return self._carrot2
        elif id == 'carrot3':
            return self._carrot3
        elif id == 'cabbage1':
            return self._cabbage1
        elif id == 'cabbage2':
            return self._cabbage2
        elif id == 'cabbage3':
            return self._cabbage3
        elif id == 'player':
            return self._player
        elif id == 'cardboard':
            return self._cardboard_trap
        elif id == 'pepper1':
            return self._pepper1
        elif id == 'pepper2':
            return self._pepper2
        elif id == 'pepper3':
            return self._pepper3
        elif id == 'tomato1':
            return self._tomato1
        elif id == 'tomato2':
            return self._tomato2
        elif id == 'tomato3':
            return self._tomato3
        elif id == 'pixel':
            return self._pixel
        elif id == 'dirt':
            return self._dirt
        elif id == 'shopTile':
            return self._shopTile
        elif id == 'shopBorderTile':
            return self._shopBorderTile
        elif id == 'grass':
            return self._grass
        elif id == 'marker':
            return self._marker





