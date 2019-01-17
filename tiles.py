import pygame
import constants
from art import *
from block import *



TILESIZE = 50
MAPWIDTH = 25
MAPHEIGHT = 14

class GrassTile(Block):
    def __init__(self):
        self.art = Art()

        super().__init__(self.art.get_image('grass'), TILESIZE, TILESIZE)

        self.is_plantable = False
        self.is_grass = True

        self.rect.x = 0
        self.rect.y = 0
        
class DirtTile(Block):
    def __init__(self):
        self.art = Art()

        super().__init__(self.art.get_image('dirt'), TILESIZE, TILESIZE)

        self.is_plantable = True
        self.is_grass = False

        self.rect.x = 0
        self.rect.y = 0
            
class ShopTile(Block):
    def __init__(self):
        self.art = Art()

        super().__init__(self.art.get_image('shopTile'), TILESIZE, TILESIZE)

        self.is_plantable = False
        self.is_grass = False

        self.rect.x = 0
        self.rect.y = 0


class ShopBorderTile(Block):
    def __init__(self):
        self.art = Art()

        super().__init__(self.art.get_image('shopBorderTile'), TILESIZE, TILESIZE)

        self.is_plantable = False
        self.is_grass = False

        self.rect.x = 0
        self.rect.y = 0


tilemap = [ [GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  DirtTile(),  GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile()],
            [GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile(), GrassTile()] ]

shopTileMap = [ [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopTile(),  ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()],
            [ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile(), ShopBorderTile()] ]
