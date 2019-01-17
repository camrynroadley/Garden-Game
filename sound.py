"""
Implements all sound objects.
"""

import pygame
import title_screen
import game_screen
import constants

from level_manager import *
from file_manager import *

class Sound():

    # creates the sound object
    def __init__(self):
        self._attack_sound = FileManager().get_sound_path('attack')
        self._eat_sound = FileManager().get_sound_path('eat')
        self._background_music = FileManager().get_sound_path('background_music')
        self._money = FileManager().get_sound_path('money')

    # retrieves sound initialized referenced by id
    def get_sound(self, id):
        if id == 'attack':
            return self._attack_sound
        elif id == 'eat':
            return self._eat_sound
        elif id == 'background_music':
            return self._background_music
        elif id == 'money':
            return self._money        
