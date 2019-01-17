import pygame, constants, pyganim

from block import *
from seedBag import *
from inventory import *
from carrot import *
from cabbage import *
from pepper import *
from tomato import *
from trap import *

class Player(Block):
 
    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """

        self.is_swinging = False #True when player attacks
        
        # Call the parent class (Block) constructor
        super().__init__(pygame.image.load('images/player.png'), 40, 40)

        #Creates the animations for left and right facing walking
        #They are tuples (requirement of pyganimation) - can't be modified in game_screen
        self.walk_anim = pyganim.PygAnimation([(self.image, 0.1),
                                               ('images/player_walk.png', 0.1)])
        self.walk_right_anim = pyganim.PygAnimation([(pygame.transform.flip(self.image, True, False), 0.1),
                                                     (pygame.transform.flip(pygame.image.load('images/player_walk.png'), True, False), 0.1)])

        #This puts the animations into a stopped position (must be started in the methods)
        self.walk_anim.stop()
        self.walk_right_anim.stop()

        #Creates the animations for attacking
        attack1 = pygame.image.load('images/attack1.png')
        attack2 = pygame.image.load('images/attack2.png')
        attack3 = pygame.image.load('images/attack3.png')
        
        self.attack_anim = pyganim.PygAnimation([(attack1, 0.1),
                                                 (attack2, 0.1),
                                                 (attack3, 0.1)])
        self.attack_right_anim = pyganim.PygAnimation([(pygame.transform.flip(attack1, True, False), 0.1),
                                                       (pygame.transform.flip(attack2, True, False), 0.1),
                                                       (pygame.transform.flip(attack3, True, False), 0.1)])

        self.attack_right_anim.stop()
        self.attack_anim.stop()

        #These have to be here because of the animation tuples
        self.moving = False
        self.right = False

 
        self.rect.x = constants.SCREEN_WIDTH/2
        self.rect.y = constants.SCREEN_HEIGHT - 300
        self.x_speed = 0
        self.y_speed = 0

        self.money = 0
        self.score = 0
        

        self.inventory = Inventory()

        
        #Plants in the game are held by the player class
        #This allows for easy transfer across levels
        self.plant_list = pygame.sprite.Group()
        self.plant_hitList = pygame.sprite.Group()
        self.trap_list = pygame.sprite.Group()

        #This allows us to cycle our items.
        self.selected = 1

        #These are to use in the inventory text in the game screen
        self.carrot_count = self.inventory.seedBag.numOfCarrotSeeds
        self.cabbage_count = self.inventory.seedBag.numOfCabbageSeeds
        self.pepper_count = self.inventory.seedBag.numOfPepperSeeds
        self.tomato_count = self.inventory.seedBag.numOfTomatoSeeds
        self.trap_count = self.inventory.trapBag.num_of_traps

       

    #these functions change the x and y speeds and start/stop animations
    def move_left(self):
        self.x_speed = -5
        self.walk_anim.play()
        self.moving = True
        self.right = False        
    def move_right(self):
        self.x_speed = 5
        self.walk_right_anim.play()
        self.moving = True
        self.right = True                                                    
    def move_up(self):
        self.y_speed = -5
        self.walk_anim.play()
        self.moving = True
    def move_down(self):
        self.y_speed = 5
        self.walk_anim.play()
        self.moving = True

    #In the below, False and stop() are in an if statement so the gardener keeps walking when two direction keys are pressed.
    def stop_x(self):
        self.x_speed = 0
        if self.y_speed == 0:
            self.moving = False
            self.walk_anim.stop()
    def stop_y(self):
        self.y_speed = 0
        if self.x_speed == 0:
            self.moving = False
            self.walk_anim.stop()

    #changes the x and y coordinates of the player
    def update_position(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        #Stop player from leaving the screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > constants.SCREEN_WIDTH - 50:
            self.rect.x = constants.SCREEN_WIDTH - 50
        if self.rect.y < 100:
            self.rect.y = 100
        if self.rect.y > constants.SCREEN_HEIGHT - 50:
            self.rect.y = constants.SCREEN_HEIGHT - 50

    #This plants items according to what they are cycled to.
    def plant(self, x, y):
        if (self.selected == 1):
            if(self.inventory.seedBag.canPlantCarrotSeed()):
                self.inventory.seedBag.plantCarrotSeed()
                carrot = Carrot(x, y)
                self.plant_list.add(carrot)
                return True
                
        elif (self.selected == 2):
            if(self.inventory.seedBag.canPlantCabbageSeed()):
                self.inventory.seedBag.plantCabbageSeed()
                cabbage = Cabbage(x, y)
                self.plant_list.add(cabbage)
                return True

        elif (self.selected == 3):
            if(self.inventory.seedBag.canPlantPepperSeed()):
                self.inventory.seedBag.plantPepperSeed()
                pepper = Pepper(x, y)
                self.plant_list.add(pepper)
                return True

        elif (self.selected == 4):
            if(self.inventory.seedBag.canPlantTomatoSeed()):
                self.inventory.seedBag.plantTomatoSeed()
                tomato = Tomato(x, y)
                self.plant_list.add(tomato)
                return True

        elif (self.selected == 5):
            if(self.inventory.trapBag.can_set_trap()):
                self.inventory.trapBag.set_trap()
                trap = Trap(x, y)
                self.trap_list.add(trap)
                return True
        
        return False

    
    #This cycles through the inventory.
    def cycle_inventory(self, i):
        self.selected = i


    #The below is called in the GameScreen to keep the inventory updated.
    def update_inventory(self):
            self.carrot_count = self.inventory.seedBag.numOfCarrotSeeds
            self.cabbage_count = self.inventory.seedBag.numOfCabbageSeeds
            self.pepper_count = self.inventory.seedBag.numOfPepperSeeds
            self.tomato_count = self.inventory.seedBag.numOfTomatoSeeds
            self.trap_count = self.inventory.trapBag.num_of_traps




