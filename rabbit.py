import pygame, constants, random, pyganim

from block import *
from art import *
from sound import *
from music import *


class Rabbit(Block):

    def __init__(self, x, y):

        self.art = Art()
        self.sound = Sound()
        self.music = Music()

        #Gets the base image
        super().__init__(self.art.get_image('bunny'), 40, 40)

        #Sets up the animation images
        run1 = self.art.get_image('run1')
        run2 = self.art.get_image('run2')
        run3 = self.art.get_image('run3')

        #Animation for the rabbit facing left
        self.rabbit_run = pyganim.PygAnimation([(self.image, 0.1),
                                                (run1, 0.1),
                                               (run2, 0.1),
                                                (run3, 0.1)])

        #Animation for the rabbit facing right
        self.rabbit_right_run = pyganim.PygAnimation([(pygame.transform.flip(self.image, True, False), 0.1),
                                                     (pygame.transform.flip(run1, True, False), 0.1),
                                                     (pygame.transform.flip(run2, True, False), 0.1),
                                                     (pygame.transform.flip(run3, True, False), 0.1)])
        
        #Animation paused to begin
        self.rabbit_run.pause()
        self.rabbit_right_run.pause()

        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.is_dead = False
        self.is_eating = False
        self.is_done_eating = True
        self.health = 10 #will depend on strength of rabbit
        self.x_speed = 0
        self.y_speed = 0

        self.start_eating_time = 0
        self.eating_time_elapsed = 0

    def go_to_plant(self, x, y):
        #moves rabbit
        self.x_speed = x - self.rect.x
        y_dist = y - self.rect.y
        length = (self.x_speed**2 + y_dist**2)**.5
        if length != 0:
            self.x_speed = self.x_speed / length
            y_dist = y_dist / length
        self.rect.x += (self.x_speed * self.speed)
        self.rect.y += (y_dist * self.speed)

        if self.x_speed > 0:
            self.rabbit_right_run.play()
        elif self.x_speed < 0:
            self.rabbit_run.play()
        else:
            self.rabbit_right_run.pause()
            self.rabbit_run.pause()

    def target_plant(self, plant_list, trap_list, tile_list):
        #picks a target, focusing on traps, and sends rabbit to target
        min_dist = 1000
        target = None
        for trap in trap_list:
            x_dist = trap.get_x_coord() - self.rect.x
            y_dist = trap.get_y_coord() - self.rect.y
            dist = ( (x_dist)**2 + (y_dist)**2 )**.5
            if min_dist > dist:
                min_dist = dist
                target = trap
                self.set_health(0)
        if target is None:
            self.rabbit_run.pause()
            for plant in plant_list:
                if plant.eatable is True:
                    x_dist = plant.get_x_coord() - self.rect.x
                    y_dist = plant.get_y_coord() - self.rect.y
                    dist = ( (x_dist)**2 + (y_dist)**2 )**.5
                    if min_dist > dist:
                        min_dist = dist
                        target = plant

        if target is not None:
            self.go_to_plant(target.get_x_coord(),target.get_y_coord())

            if (pygame.sprite.collide_rect(self, target) and self.is_done_eating):
                self.is_eating = True
                self.is_done_eating = False
                return target        

    #Removes plant from list if collision after certain amount of time (set in game screen)
    def eat_plant(self, plant_list, tile_list):
            for plant in plant_list:
                if pygame.sprite.collide_rect(self, plant):
                    self.music.play_once(self.sound.get_sound("eat"))
                    plant.kill()
            for tile in tile_list:
                if pygame.sprite.collide_rect(self, tile):
                    tile.is_plantable = True
            self.is_eating = False
            self.is_done_eating = True


    #Returns boolean whether or not rabbit was hurt
    #False means rabbit should be removed
    def hurt_rabbit(self):
        if (self.health > 1):
            self.health += -1
            return True
        else :
            pass
            return False

    def set_health(self, h):
        self.health = h

    def set_eating_time(self):
        self.start_eating_time = pygame.time.get_ticks() + 5000
        self.is_eating = False
