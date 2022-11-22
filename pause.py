import pygame, sys
from button import Button

SCREEN = pygame.display.set_mode((1280, 720))
font = pygame.font.Font('Assets/Mainmenu/font/font.ttf',32)

class Pause():
    def pause_menu(self):
        text_surf = font.render('Pause',False,'white')
        text_rect = text_surf.get_rect(center = (1280/2 , 720/2))
        SCREEN.blit(text_surf,text_rect)
