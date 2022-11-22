import pygame

SCREEN = pygame.display.set_mode((1280, 720))

class Item(pygame.sprite.Sprite):
    def __init__(self,pos,groups,name):
        super().__init__(groups)
        self.sprite_type = 'item'
        self.image = pygame.image.load(name).convert_alpha()
        self.image = pygame.transform.scale(self.image,(15,25))
        self.rect = self.image.get_rect()
        self.rect.center = pos