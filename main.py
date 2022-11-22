import pygame, sys
from button import Button
from settings import *
from level import Level
from enemy import Enemy
from player import Player
import json
   
scoreboard = {}

try:
    with open('score.json') as score_file:
        scoreboard = json.load(score_file)
except:
    pass

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THE LOPBURI")
icon = pygame.image.load('back_icon/icon.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('Assets/Mainmenu/font/joystix.ttf',32)

clock = pygame.time.Clock()


BG = pygame.image.load('Assets/tileset/JG BG.jpg')
BG = pygame.transform.scale(BG,(WIDTH,HEIGHT))

def get_font(size):
    return pygame.font.Font('Assets/Mainmenu/font/joystix.ttf', size)

def main_menu():
    while True:
        text_surf = get_font(18).render('65010815 Pattarachai Wannasuntad',False,'black')
        text_rect = text_surf.get_rect(center = (1280 - text_surf.get_width() - 160, 720 - text_surf.get_height() - 5))
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(text_surf,text_rect)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("THE LOPBURI", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/Mainmenu/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCORE_BUTTON = Button(image=pygame.image.load("Assets/Mainmenu/Options Rect.png"), pos=(640, 400), 
                            text_input="SCORE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/Mainmenu/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, SCORE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):     
                    play()
                if SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    score()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def play():
    level = Level()
    while True:   
        if level.player_alive == False:
            text_input(level.point)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    level.toggle_menu()
                if event.key == pygame.K_9:
                    level.force_death()
                    
        level.run()
        pygame.display.update()
        clock.tick(FPS)

def score():
    font = get_font(40)
    #level = Level()
    while True:
        display_surf = pygame.display.get_surface()
        SCORE_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG,(0,0))

        SCORE_BACK = Button(image=None, pos = (WIDTH-120,600),
                            text_input='back', font=get_font(45), base_color = 'Black', hovering_color='Green')
        SCORE_BACK.changeColor(SCORE_MOUSE_POS)
        SCORE_BACK.update(SCREEN)

        # read  
        with open('score.json', 'r') as score_file:
            player_score = json.load(score_file)
        
        offset = 0
        count = 0
        sorted_name = sorted(player_score.items(), key=lambda x:x[1], reverse=True)
        sorted_dict = dict(sorted_name)
        name = list(sorted_dict.keys())

        subject = get_font(70).render('High Score', False, 'gold')
        subject_rect = subject.get_rect(center = ((1280 // 2), 100))
        pygame.draw.rect(display_surf, UI_BG_COLOR,subject_rect.inflate(20, 0))
        display_surf.blit(subject, subject_rect)

        for key in name:
            if count <= 4:
                image = pygame.image.load('Assets/tileset/JG BG.jpg')
                image = pygame.transform.scale(image,(WIDTH,HEIGHT))
                text_surf = font.render(key, False, 'white')
                text_rect = text_surf.get_rect(topright = ((1280 // 2) - 100, 200 + offset))
                score_surf = font.render(str(int(sorted_dict[key])), False, 'black')
                score_rect = score_surf.get_rect(topleft = ((1280 // 2) + 100, 200 + offset))
                
                offset += 80
                count += 1
                pygame.draw.rect(display_surf, UI_BG_COLOR, text_rect.inflate(20, 0))
                display_surf.blit(text_surf, text_rect)
                display_surf.blit(score_surf, score_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SCORE_BACK.checkForInput(SCORE_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def gameOver():
    while True:
        font = get_font(120)
        text_surf = font.render('GAME OVER',False,'brown')
        text_rect = text_surf.get_rect(center = (640 , 350))
        # level = Level()

        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(text_surf, text_rect)
        
        # OVER_MOUSE_POS = pygame.mouse.get_pos()
        # OVER_BACK = Button(image=None, pos=(640, 500), 
        #                     text_input="PLAY AGAIN", font=get_font(45), base_color="Black", hovering_color="Green")

        # OVER_BACK.changeColor(OVER_MOUSE_POS)
        # OVER_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if OVER_BACK.checkForInput(OVER_MOUSE_POS):
            #         main_menu()

        pygame.display.update()

def text_input(score):
    player_name = ''
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                       player_name = player_name[:-1]
                    elif event.key == pygame.K_RETURN and len(player_name) >= 1:
                        scoreboard[player_name] = score
                        with open('score.json', 'w') as score_file:
                            json.dump(scoreboard,score_file)
                        gameOver()
                    else:
                        player_name += event.unicode
        font = get_font(30)
        SCREEN.fill(UI_BG_COLOR)
        input_surf = font.render('Input your name',False, 'gold')
        input_rect = input_surf.get_rect(center = (WIDTH // 2, 200))
        pygame.draw.rect(SCREEN, 'black', input_rect.inflate(20,20))
        SCREEN.blit(input_surf,input_rect)
        name_surf = font.render(player_name, False, 'gold')
        name_rect = name_surf.get_rect(center = (WIDTH // 2, HEIGHT // 2 ))
        pygame.draw.rect(SCREEN, UI_BG_COLOR, name_rect.inflate(20, 20))
        SCREEN.blit(name_surf, name_rect)
        pygame.display.update()

main_menu()