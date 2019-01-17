'''
Shop screen
Player moves in shop and stands on items to buy
Player advances to next level after visiting shop
'''

import pygame
import constants
import game_screen
import title_screen
import tiles

from screen import *
from level_manager import *
from screen import *
from carrot import *
from cabbage import *
from tomato import *
from pepper import *
from trap import *
from sound import *
from music import *
from player import *

class ShopScreen(Screen):
    def __init__(self, player, level):

        super().__init__()

        self.sound = Sound()
        self.music = Music()
        
        self.font = pygame.font.SysFont('Calibri', 25, True, False)

        #Sprite lists for the shop        
        self.all_sprites_list = pygame.sprite.Group()
        self.shop_list = pygame.sprite.Group()
        self.playerSprite = pygame.sprite.Group()
        self.shopTiles = pygame.sprite.Group()

        #Puts in the tiles
        for row in range(tiles.MAPHEIGHT):
            for column in range(tiles.MAPWIDTH):
                tiles.shopTileMap[row][column].rect.y = row*tiles.TILESIZE
                tiles.shopTileMap[row][column].rect.x = column*tiles.TILESIZE
                self.shopTiles.add(tiles.shopTileMap[row][column])

        #Adds an image for carrot, cabbage, pepper, tomato, and trap
        carrot = Carrot(520, 250)
        carrot.image = carrot.art.get_image('carrot3')
        self.shop_list.add(carrot)
        self.all_sprites_list.add(carrot)
        self.carrot_text = self._font.render("Carrot: $1", True, constants.BLACK)

        cabbage = Cabbage(680, 250)
        cabbage.image = cabbage.art.get_image('cabbage3')
        self.shop_list.add(cabbage)
        self.all_sprites_list.add(cabbage)
        self.cabbage_text = self._font.render("Cabbage: $2", True, constants.BLACK)

        pepper = Pepper(520, 400)
        pepper.image = pepper.art.get_image('pepper3')
        self.shop_list.add(pepper)
        self.all_sprites_list.add(pepper)
        self.pepper_text = self._font.render("Pepper: $3", True, constants.BLACK)

        tomato = Tomato(680, 400)
        tomato.image = tomato.art.get_image('tomato3')
        self.shop_list.add(tomato)
        self.all_sprites_list.add(tomato)
        self.tomato_text = self._font.render("Tomato: $4", True, constants.BLACK)

        trap = Trap(820, 325)
        trap.image = trap.art.get_image("cardboard")
        self.shop_list.add(trap)
        self.all_sprites_list.add(trap)
        self.trap_text = self._font.render("Trap: $5", True, constants.BLACK)

        #Some instructions text
        self.instruct_text = self._font.render("Press space to buy when character is on top of item.", True, constants.BLACK)
        self.play_instruct = self.font.render('Press p to exit shop.', True, constants.BLACK)

        #Our player
        self.player = player

        #Not sure if we need right and up with animation
        self.right = False
        self.up = False

        self.playerSprite.add(player)


        self._text = self.font.render("Shop",True,constants.BLACK, [constants.SCREEN_WIDTH / 2, 10])

        self.buy = False
        self.level = level + 1

        self.right_keyDown = False
        self.up_keyDown = False
        self.left_keyDown = False
        self.down_keyDown = False

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:         
                LevelManager().leave_level()
                LevelManager().load_level(title_screen.TitleScreen())
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.move_left()
                self.left_keyDown = True
                # self.pixel.move_left()
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.move_right()
                self.right_keyDown = True
                # self.pixel.move_right()
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self.player.move_up()
                self.up_keyDown = True
                # self.pixel.move_up()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.player.move_down()
                self.down_keyDown = True
                #self.pixel.move_down()
            elif event.key == pygame.K_SPACE:
                self.buy = True
            elif event.key == pygame.K_p:
                LevelManager().leave_level()
                self.player.inventory.purse.money = 0
                LevelManager().load_level(game_screen.GameScreen(self.player, self.level))
            
            
                
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                self.left_keyDown = False
                if(not self.right_keyDown):
                    self.player.stop_x()
                else:
                    self.player.move_right()
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                self.right_keyDown = False
                if (not self.left_keyDown):
                    self.player.stop_x()
                else:
                    self.player.move_left()
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self.up_keyDown = False
                if(not self.down_keyDown):
                    self.player.stop_y()
                else:
                    self.player.move_down()
            elif event.key == pygame.K_DOWN  or event.key == pygame.K_s:
                self.down_keyDown = False
                if (not self.up_keyDown):
                    self.player.stop_y()
                else:
                    self.player.move_up()
                
    
    def update(self):
        self.player.update_position()

        #Checks for collisions and buys an item
        for item in self.shop_list:
            if pygame.sprite.collide_rect(item, self.player) and self.player.inventory.purse.canBuy(item.cost) and self.buy == True:
                self.player.inventory.purse.buy(item.cost)
                self.music.play_once(self.sound.get_sound("money"))
                if isinstance(item, Carrot):
                    self.player.inventory.seedBag.numOfCarrotSeeds += 1
                    self.buy = False
                if isinstance(item, Cabbage):
                    self.player.inventory.seedBag.numOfCabbageSeeds += 1
                    self.buy = False
                if isinstance(item, Pepper):
                    self.player.inventory.seedBag.numOfPepperSeeds += 1
                    self.buy = False
                if isinstance(item, Tomato):
                    self.player.inventory.seedBag.numOfTomatoSeeds += 1
                    self.buy = False
                if isinstance(item, Trap):
                    self.player.inventory.trapBag.num_of_traps += 1
                    self.buy = False

        
    def draw(self, screen):
        #Draws the tiled background
        self.shopTiles.draw(screen)

        # draws everything needed for the hotbar
        screen.blit(pygame.image.load('images/top_hotbar.png').convert_alpha(), [268, 0])
        carrot_count = self._hotbar_plant_font.render(str(self.player.inventory.seedBag.numOfCarrotSeeds), True, constants.HOTBAR_TEXT)
        screen.blit(carrot_count, [616, 58])
        cabbage_count = self._hotbar_plant_font.render(str(self.player.inventory.seedBag.numOfCabbageSeeds), True, constants.HOTBAR_TEXT)
        screen.blit(cabbage_count, [672, 58])
        pepper_count = self._hotbar_plant_font.render(str(self.player.inventory.seedBag.numOfPepperSeeds), True, constants.HOTBAR_TEXT)
        screen.blit(pepper_count, [728, 58])
        tomato_count = self._hotbar_plant_font.render(str(self.player.inventory.seedBag.numOfTomatoSeeds), True, constants.HOTBAR_TEXT)
        screen.blit(tomato_count, [784, 58])
        trap_count = self._hotbar_plant_font.render(str(self.player.inventory.trapBag.num_of_traps), True, constants.HOTBAR_TEXT)
        screen.blit(trap_count, [840, 58])
        money_count = self._hotbar_font.render(str(self.player.inventory.purse.money), True, constants.HOTBAR_TEXT)
        screen.blit(money_count, [395, 19])
        score_count = self._hotbar_font.render(str(self.player.score), True, constants.HOTBAR_TEXT)
        screen.blit(score_count, [395, 52])

        # Draw my title text
        screen.blit(self._text, [0, 10])


        #draw sprites
        self.all_sprites_list.draw(screen)
        
        #Draw instructions
        screen.blit(self.play_instruct, [525, 120])
        screen.blit(self.instruct_text, [465, 150])

        #Draw item text
        screen.blit(self.carrot_text, [515, 235])
        screen.blit(self.cabbage_text, [670, 235])
        screen.blit(self.pepper_text, [515, 385])
        screen.blit(self.tomato_text, [675, 385])
        screen.blit(self.trap_text, [825, 310])
        
        # Moves the player with animation
        if self.player.moving == False and self.player.right == False:
            screen.blit(self.player.image, [self.player.rect.x, self.player.rect.y])
        elif self.player.moving == False and self.player.right == True:
            screen.blit(pygame.transform.flip(self.player.image, True, False), [self.player.rect.x, self.player.rect.y])        
        elif self.player.moving == True and self.player.right == False:
            self.player.walk_anim.blit(screen, [self.player.rect.x, self.player.rect.y])
        else:
            self.player.walk_right_anim.blit(screen, [self.player.rect.x, self.player.rect.y])
                                
