#Displays the credits

import pygame
import constants

from level_manager import *
from art import *

class CreditsScreen():
    def __init__(self):
        
        title_font = pygame.font.SysFont('castellar', 48, True, False)
        credit_font = pygame.font.SysFont('mangal', 20, True, False)
        instruction_font = pygame.font.SysFont('mangal', 32, True, False)
        self._text = title_font.render("Credits",True,constants.BLACK)
        self._instruct_text1 = instruction_font.render("Press escape to return to the title screen.", True, constants.BLACK)
        self._credit_text1 = credit_font.render("Game designed by Monica Timmerman, Jack Olson,"
                                                       + " Carrie Mannilla, Bryant Lennick, Camryn Roadley, & Dan Nygard", True, constants.BLACK)
        self._credit_text2 = credit_font.render("Game background music is \"Awesome Call\" by Kevin MacLeod (incompetech.com) ",True, constants.BLACK)
        self._credit_text3 = credit_font.render("Licensed under Creative Commons: By Attribution 3.0 License http://creativecommons.org/licenses/by/3.0/", True, constants.BLACK)
        self._credit_text4 = credit_font.render("Sound effects from free sounds library at https://www.partnersinrhyme.com/pir/PIRsfx.shtml:", True, constants.BLACK)
        self._credit_text5 = credit_font.render("Rabbit attack: https://www.partnersinrhyme.com/soundfx/fight_sounds/fight_punch_wav.shtml", True, constants.BLACK)
        self._credit_text6 = credit_font.render("Harvest sound: https://www.partnersinrhyme.com/soundfx/office_sounds/office_cash-register2_wav.shtml", True, constants.BLACK)

        self._credit_text7 = credit_font.render("All game art by Bryant Lennick using Piskel (https://www.piskelapp.com/).",True, constants.BLACK)
        self._credit_text8 = credit_font.render("Sprite animation created using PygAnim, Copyright 2014 Al Sweigart", True, constants.BLACK)

        

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()

    #No need to do anything here, unless we've got some animation
    def update(self):
        pass
        
    def draw(self, screen):
        # Clear the screen
        screen.blit(pygame.image.load('images/background.png').convert_alpha(), [0, 0])
        
        # Draw my credits text!
        screen.blit(self._text, [380, 150])
        screen.blit(self._credit_text1, [210, 200])
        screen.blit(self._credit_text2, [210, 225])
        screen.blit(self._credit_text3, [225, 250])
        screen.blit(self._credit_text4, [210, 275])
        screen.blit(self._credit_text5, [225, 300])
        screen.blit(self._credit_text6, [225, 325])
        screen.blit(self._credit_text7, [210, 350])
        screen.blit(self._credit_text8, [210, 375])

        screen.blit(self._instruct_text1, [210, 450])
        
