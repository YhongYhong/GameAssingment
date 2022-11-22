import pygame
from settings import *
from support import import_folder
from math import sin

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move_player(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            # print(self.direction)
            
        if (self.hitbox.x > (WIDTH_PLAYER/2) or self.direction.x > 0) :					# setting for make player in the map //custom
            if (self.hitbox.x < (WIDTH_MAP-WIDTH_PLAYER/2) or self.direction.x < 0):	# setting for make player in the map
                self.hitbox.x += self.direction.x * speed
                self.collision('horizontal')
        if (self.hitbox.y > (HEIGHT_PLAYER/2) or self.direction.y > 0) :				# setting for make player in the map
            if (self.hitbox.y < (HEIGHT_MAP-HEIGHT_PLAYER/2) or self.direction.y < 0):	# setting for make player in the map
                self.hitbox.y += self.direction.y * speed
                self.collision('vertical')
        self.rect.center = self.hitbox.center

    def move_enemy(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        if self.direction.x > 0:
            self.hitbox.x += self.direction.x * speed
        if self.direction.x < 0:
            self.hitbox.x += self.direction.x * (speed-0.95)    # debug enemy run
        self.collision('horizontal')
        if self.direction.y > 0:
            self.hitbox.y += self.direction.y * speed
        if self.direction.y < 0:
            self.hitbox.y += self.direction.y * (speed-0.95)    # debug enemy run
        self.collision('vertical')
        self.rect.center = self.hitbox.center
                
    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0
