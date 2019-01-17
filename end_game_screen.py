"""
End game screen. Gives final score and allows to play again.
"""


import game_screen, constants, title_screen
from level_manager import *
from screen import *
from player import *

class EndGameScreen(Screen):
    #Takes two additional parameters to provide the score and level
    def __init__(self, num, day):
        super().__init__()

        GameOver_font = pygame.font.SysFont('castellar', 48, True, False)
        information_font = pygame.font.SysFont('mangal', 32, True, False)


        self._text1 = GameOver_font.render("Game Over",True,constants.BLACK)
        self._text2 = GameOver_font.render("Final Score: " + str(num), True, constants.BLACK)
        self._text3 = information_font.render("Press P to play again.",True,constants.BLACK)
        self._text4 = information_font.render("Press Esc to return to Title Screen.", True, constants.BLACK)
        self._text5 = information_font.render("You survived " + str(day) + " days.", True, constants.BLACK)
        if day == 1:
            self._text5 = information_font.render("You survived " + str(day) + " day.", True, constants.BLACK)

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
                LevelManager().load_level(title_screen.TitleScreen())
            if event.key == pygame.K_p:
                LevelManager().leave_level()
                player = Player()
                LevelManager().load_level(game_screen.GameScreen(player, 1))


    #No need to do anything here, unless we've got some animation
    def update(self):
        pass

    def draw(self, screen):
        # Draw background and text
        screen.fill(constants.LIGHT_BROWN)
        screen.blit(pygame.image.load('images/background.png').convert_alpha(), [0,0])

        screen.blit(self._text1, [430, 120])
        screen.blit(self._text2, [380, 180])
        screen.blit(self._text3, [300, 420])
        screen.blit(self._text4, [300, 450])
        screen.blit(self._text5, [490, 250])
