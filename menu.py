import pygame, sys
from button import Button
from main import Game
from level import Level

pygame.init()

WIDTH,HEIGHT = (1280, 720)

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT)) # SizeScreen
pygame.display.set_caption("The Lowburi") # ProgramName

BG = pygame.image.load("Assets/ForestBG.png") # BGPic
BG = pygame.transform.scale(BG,(WIDTH,HEIGHT))

level = Level()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Assets/MainMenu/font/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        game = Game()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        pygame.quit()
                        sys.exit()
                    # if event.key == pygame.K_1:
                    #     level.player_alive = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            game.run()
            pygame.display.update()
            clock.tick(FPS)
        
        # SCREEN.fill("black")

        # PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # PLAY_BACK = Button(image=None, pos=(640, 460), 
        #                     text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        # PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        # PLAY_BACK.update(SCREEN)

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
        #             main_menu()

        # pygame.display.update()
    
def credit():
    while True:
        CREDIT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        CREDIT_TEXT = get_font(35).render("65010815 Pattarachai Wannasuntad", True, "Black")
        CREDIT_RECT = CREDIT_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(CREDIT_TEXT, CREDIT_RECT)

        CREDIT_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        CREDIT_BACK.changeColor(CREDIT_MOUSE_POS)
        CREDIT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDIT_BACK.checkForInput(CREDIT_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("The Lopburi", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/MainMenu/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        CREDIT_BUTTON = Button(image=pygame.image.load("Assets/MainMenu/Options Rect.png"), pos=(640, 400), 
                            text_input="CREDITS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/MainMenu/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CREDIT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credit()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()