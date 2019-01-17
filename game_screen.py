'''
Game screen code
Player moves around, plants crops and traps
Player defends garden from incoming rabbits
'''

import pygame, pyganim
import constants
import shop_screen
import title_screen

import tiles

from level_manager import *
from screen import *
from block import *
from player import *
from rabbit import *
from carrot import *
from shop_screen import *
import seedBag
from title_screen import *
from end_game_screen import *
from pixel import *
from hoe_hitbox import *

import datetime
import time

class GameScreen(Screen):
    def __init__(self, player = Player(), level = 1):

        super().__init__()
        #Lists that handle sprites on the screen
        self.all_sprites_list = pygame.sprite.Group()
        self.rabbit_list = pygame.sprite.Group()
        self.tile_list = pygame.sprite.Group()
        #DO NOT CHANGE TILE VALUES IN grass_tile_list
        self.grass_tile_list = pygame.sprite.Group() 
        self.playerSprite = pygame.sprite.Group()

        self.player = player
        self.level = level
        self.pixel = Pixel()
        self.sound = Sound()
        self.music = Music()
        self.music.play_repeat(self.sound.get_sound("background_music"))

        #Goal is set to this
        self.goal = (self.level - 1) * 75 + 25
        #self.all_sprites_list.add(self.player)
        self.all_sprites_list.add(self.pixel)

        #map the tiles 
        for row in range(tiles.MAPHEIGHT):
            for column in range(tiles.MAPWIDTH):
                tiles.tilemap[row][column].rect.y = row*tiles.TILESIZE
                tiles.tilemap[row][column].rect.x = column*tiles.TILESIZE
                if (tiles.tilemap[row][column].is_grass):
                    self.grass_tile_list.add(tiles.tilemap[row][column])
                else:
                    self.tile_list.add(tiles.tilemap[row][column])

        rabbit = Rabbit(-50,-50)
        rabbit.speed = rabbit.speed + self.level*(.5)
        self.rabbit_list.add(rabbit)

        #Set up the level's time: 60 seconds per level
        self.time = pygame.time.get_ticks()//1000
        self.time_remaining = 60 
        #Counter helps control the countown within the game loop.
        self.counter = 100000

        self.right_keyDown = False
        self.up_keyDown = False
        self.left_keyDown = False
        self.down_keyDown = False

        #What level we are on (defaults to 1)
        self.level = level

        #Hitbox object, is off screen when not in use
        self.hitbox = HoeHitbox()
        self.hitbox.rect.x = -10
        self.hitbox.rect.y = -10

        self.hit_time_start = 0
        self.hit_time_elapsed = 0

        self.rabbit_spawn_rate = 150 - level*10
        

    def handle_keyboard_event(self, event):
        #KEYDOWN EVENTS
        if event.type == pygame.KEYDOWN:
            #ESCAPE TO TITLE SCREEN
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
                self.player = Player()
                LevelManager().load_level(title_screen.TitleScreen())
                for tile in self.tile_list:
                    tile.is_plantable = True

            #F TO ATTACK
            elif event.key == pygame.K_f:
                self.player.is_swinging = True
                self.hit_time_start = pygame.time.get_ticks()
                #starts the attack animation
                self.player.attack_anim.play()
                self.player.attack_right_anim.play()

            #MOVEMENT LEFT, RIGHT, UP, DOWN
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.move_left()
                self.left_keyDown = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.move_right()
                self.right_keyDown = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self.player.move_up()
                self.up_keyDown = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.player.move_down()
                self.down_keyDown = True
            #CYCLE INVENTORY
            elif event.key == pygame.K_1:
                self.player.cycle_inventory(1)
            elif event.key == pygame.K_2:
                self.player.cycle_inventory(2)
            elif event.key == pygame.K_3:
                self.player.cycle_inventory(3)
            elif event.key == pygame.K_4:
                self.player.cycle_inventory(4)
            elif event.key == pygame.K_5:
                self.player.cycle_inventory(5)
            elif event.key == pygame.K_SPACE:
                for tile in self.tile_list:
                    if pygame.sprite.collide_rect(self.pixel, tile) and tile.is_plantable == True:
                        planted = self.player.plant(tile.rect.x, tile.rect.y)
                        if (planted):
                            tile.is_plantable = False
                            
        #KEYUP EVENTS 
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

        #Update player position
        self.player.update_position()
        #Pixel is used to track which tile player is on
        self.pixel.rect.x = self.player.rect.x + 25
        self.pixel.rect.y = self.player.rect.y + 25
        self.pixel.update_position()
        
        #update hitbox position
        if self.player.is_swinging == True:
            self.hitbox.rect.x = self.player.rect.x + 25
            self.hitbox.rect.y = self.player.rect.y
            
            #makes hitbox disappear after 250 milliseconds
            self.hit_time_elapsed = pygame.time.get_ticks() - self.hit_time_start
            if self.hit_time_elapsed > 250:            
                self.player.is_swinging = False
                self.hitbox.rect.x = -10
                self.hitbox.rect.y = -10

        #Update each rabbit's target
        for rabbit in self.rabbit_list:
                rabbit.target_plant(self.player.plant_list, self.player.trap_list, self.tile_list)
                if (rabbit.is_eating):
                    rabbit.start_eating_time = pygame.time.get_ticks() + 1800
                    rabbit.is_eating = False
                if ( pygame.time.get_ticks() > rabbit.start_eating_time and rabbit.start_eating_time != 0):  
                    rabbit.eat_plant(self.player.plant_list, self.tile_list)
                    
                

        #Keep the plants growing!
        for plant in self.player.plant_list:
            plant.grow()
            #Handle harvesting
            if pygame.sprite.collide_rect(self.pixel, plant) and plant.harvestable == True:
                self.player.inventory.purse.money += plant.sell_value
                self.player.score += plant.sell_value
                self.music.play_once(self.sound.get_sound("money"))
                for tile in self.tile_list:
                    if pygame.sprite.collide_rect(plant, tile):
                        tile.is_plantable = True
                self.player.plant_list.remove(plant)
                

        self.player.plant_list.update()
        
        for trap in self.player.trap_list:
            if(trap.remove()==False):
                for tile in self.tile_list:
                    if pygame.sprite.collide_rect(trap, tile):
                        tile.is_plantable = True
                self.player.trap_list.remove(trap)
                

        #Level is over after amount of time (this can be changed)
        time_alive = pygame.time.get_ticks()//1000
        
        if (self.time + time_alive) > self.counter:
            self.time_remaining -= 1
        if self.time_remaining == 0:
            #If you make the goal, go to the shop (and next level)
            if self.goal <= self.player.inventory.purse.money:
                pygame.time.delay(1000)
                LevelManager().leave_level()
                LevelManager().load_level(ShopScreen(self.player, self.level))
            #If you do not make the goal, go to the end game screen
            else:
                LevelManager().leave_level()
                LevelManager().load_level(EndGameScreen(self.player.score, self.level - 1))
                for tile in self.tile_list:
                    tile.is_plantable = True
        #Counter is updated following the if statements above
        self.counter = self.time + time_alive

        #Using sprite groups and collide_rect to deal with rabbit collisions.
        for rabbit in self.rabbit_list:
            if (self.player.is_swinging == True):
                if pygame.sprite.collide_rect(self.hitbox, rabbit):
                    self.rabbit_list.remove(rabbit)
                    self.music.play_once(self.sound.get_sound("attack"))
                    self.player.score += 2
            for trap in self.player.trap_list:
                if pygame.sprite.collide_rect(trap, rabbit):
                    self.rabbit_list.remove(rabbit)
                    self.player.score += 1
                    for tile in self.tile_list:
                        if pygame.sprite.collide_rect(trap, tile):
                            tile.is_plantable = True
                    self.player.trap_list.remove(trap)

        #This updates the inventory so it can be displayed in draw()
        self.player.update_inventory()
        
        #Make more rabbits!
        if (17 == random.randint(1,self.rabbit_spawn_rate)):
            num = random.randint(1,4)
            if (num == 1):
                rabbit = Rabbit(-50, random.randint(0,constants.SCREEN_HEIGHT))
                rabbit.speed = rabbit.speed + self.level*(.5)            
                self.rabbit_list.add(rabbit)
            if (num == 2):
                rabbit = Rabbit(random.randint(0,constants.SCREEN_WIDTH), -50)
                rabbit.speed = rabbit.speed + self.level*(.5)
                self.rabbit_list.add(rabbit)
            if (num == 3):
                rabbit = Rabbit(constants.SCREEN_WIDTH + 50, random.randint(0,constants.SCREEN_HEIGHT))
                rabbit.speed = rabbit.speed + self.level*(.5)
                self.rabbit_list.add(rabbit)
            if (num == 4):
                rabbit = Rabbit(random.randint(0,constants.SCREEN_WIDTH), constants.SCREEN_HEIGHT +50)
                rabbit.speed = rabbit.speed + self.level*(.5)
                self.rabbit_list.add(rabbit)

    def draw(self, screen):
        
        self.tile_list.draw(screen)
        self.grass_tile_list.draw(screen)

        screen.blit(pygame.image.load('images/top_hotbar.png').convert_alpha(), [268, 0])
        if (self.player.selected == 1):
            screen.blit(pygame.image.load('images/marker_hotbar.png').convert_alpha(), [constants.MARKER_X1, constants.MARKER_Y])
        elif (self.player.selected == 2):
            screen.blit(pygame.image.load('images/marker_hotbar.png').convert_alpha(), [constants.MARKER_X2, constants.MARKER_Y])
        elif (self.player.selected == 3):
            screen.blit(pygame.image.load('images/marker_hotbar.png').convert_alpha(), [constants.MARKER_X3, constants.MARKER_Y])
        elif (self.player.selected == 4):
            screen.blit(pygame.image.load('images/marker_hotbar.png').convert_alpha(), [constants.MARKER_X4, constants.MARKER_Y])
        elif (self.player.selected == 5):
            screen.blit(pygame.image.load('images/marker_hotbar.png').convert_alpha(), [constants.MARKER_X5, constants.MARKER_Y])
        
        #Draws an inventory tracker
        carrot_text = self._hotbar_plant_font.render(str(self.player.carrot_count), True, constants.HOTBAR_TEXT)
        screen.blit(carrot_text, [616, 58])
        cabbage_text = self._hotbar_plant_font.render(str(self.player.cabbage_count), True, constants.HOTBAR_TEXT)
        screen.blit(cabbage_text, [672, 58])
        pepper_text = self._hotbar_plant_font.render(str(self.player.pepper_count), True, constants.HOTBAR_TEXT)
        screen.blit(pepper_text, [728, 58])
        tomato_text = self._hotbar_plant_font.render(str(self.player.tomato_count), True, constants.HOTBAR_TEXT)
        screen.blit(tomato_text, [784, 58])
        trap_text = self._hotbar_plant_font.render(str(self.player.trap_count), True, constants.HOTBAR_TEXT)
        screen.blit(trap_text, [840, 58])

        #Draw hotbar stuff
        money_text = self._hotbar_font.render(str(self.player.inventory.purse.money), True, constants.HOTBAR_TEXT)
        screen.blit(money_text, [395, 19])
        timer_text = self._hotbar_font.render(str(self.time_remaining), True, constants.HOTBAR_TEXT)
        screen.blit(timer_text, [907, 51])
        goal_text = self._hotbar_font.render(str(self.goal), True, constants.HOTBAR_TEXT)
        screen.blit(goal_text, [508, 51])
        score_text = self._hotbar_font.render(str(self.player.score), True, constants.HOTBAR_TEXT)
        screen.blit(score_text, [395, 52])

        #Instruction text
        instruct_text4 = self._font.render('Press f to attack bunnies.', True, constants.HOTBAR_TEXT)
        screen.blit(instruct_text4, [10, 635])
        instruct_text1 = self._font.render("Press 1 - 5 to cycle through your crops and traps.", True, constants.HOTBAR_TEXT)
        screen.blit(instruct_text1, [10, 650])
        instruct_text2 = self._font.render("Press space to plant selected crop or trap.", True, constants.HOTBAR_TEXT)
        screen.blit(instruct_text2, [10, 665])
        instruct_text3 = self._font.render('Walk over grown crops to harvest and make money.', True, constants.HOTBAR_TEXT)
        screen.blit(instruct_text3, [10, 680])

        #Tells the player what level it is
        day_text = self._font.render('Day: ' + str(self.level), True, constants.HOTBAR_TEXT)
        screen.blit(day_text, [200, 585])

        # Draw everything
        self.all_sprites_list.draw(screen)
        self.player.plant_list.draw(screen)
        self.player.trap_list.draw(screen)

        #Rabbit animation is blitted here
        for rabbit in self.rabbit_list:
            if(rabbit.x_speed > 0):
                rabbit.rabbit_right_run.blit(screen, [rabbit.rect.x, rabbit.rect.y])                
            else:
                rabbit.rabbit_run.blit(screen, [rabbit.rect.x, rabbit.rect.y])

        # Draws the player with animation if moving, draws base image if stopped
        # Controls player facing either left or right
        if self.player.moving == False and self.player.right == False:          
            if self.player.is_swinging == True:
                self.player.attack_anim.blit(screen, [self.player.rect.x, self.player.rect.y])
            else:
                screen.blit(self.player.image, [self.player.rect.x, self.player.rect.y])

        elif self.player.moving == False and self.player.right == True:
            if self.player.is_swinging == True:
                self.player.attack_right_anim.blit(screen, [self.player.rect.x, self.player.rect.y])
            else:
                screen.blit(pygame.transform.flip(self.player.image, True, False), [self.player.rect.x, self.player.rect.y])        

        elif self.player.moving == True and self.player.right == False:
            if self.player.is_swinging == True:
                self.player.attack_anim.blit(screen, [self.player.rect.x, self.player.rect.y])
            else:
                self.player.walk_anim.blit(screen, [self.player.rect.x, self.player.rect.y])

        else:
            if self.player.is_swinging == True:
                self.player.attack_right_anim.blit(screen, [self.player.rect.x, self.player.rect.y])
            else:
                self.player.walk_right_anim.blit(screen, [self.player.rect.x, self.player.rect.y])

        
        
 
