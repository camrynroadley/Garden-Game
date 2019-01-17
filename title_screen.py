import pygame
import constants

from level_manager import *
from game_screen import *
from credits_screen import *
from player import *
from screen import *

class TitleScreen(Screen):
    def __init__(self):
        
        title_font = pygame.font.SysFont('castellar', 48, True, False)
        instruction_font = pygame.font.SysFont('mangal', 32, True, False)

        self._text = title_font.render("GARDEN GAME",True,constants.BLACK)

        self.play_instruct = instruction_font.render('Press p to play.', True, constants.BLACK)
        self.play_instruct2 = instruction_font.render('Press c for credits.', True, constants.BLACK)


        self.instruct_text1 = instruction_font.render("Press 1 - 5 to cycle through your crops and traps.", True, constants.BLACK)
        self.instruct_text2 = instruction_font.render("Press space to plant selected crop or trap.", True, constants.BLACK)
        self.instruct_text3 = instruction_font.render('Walk over grown crops to harvest and make money.', True, constants.BLACK)
        self.instruct_text4 = instruction_font.render('Press f to attack bunnies.', True, constants.BLACK)
        self.player = Player()


        

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
            elif event.key == pygame.K_p:
                LevelManager().leave_level()
                LevelManager().load_level(GameScreen(self.player, 1))
            elif event.key == pygame.K_c:
                LevelManager().load_level(CreditsScreen())

    #No need to do anything here, unless we've got some animation
    def update(self):
        pass
        
    def draw(self, screen):
        # Clear the screen
        screen.blit(pygame.image.load('images/background.png').convert_alpha(), [0, 0])
     
        # Draw my title text!
        screen.blit(self._text, [380, 150])
        screen.blit(self.play_instruct, [510, 320])
        screen.blit(self.play_instruct2, [510, 350])
        screen.blit(self.instruct_text4, [300, 420])
        screen.blit(self.instruct_text1, [300, 450])
        screen.blit(self.instruct_text2, [300, 480])
        screen.blit(self.instruct_text3, [300, 510])
