import pygame, sys
import json
from config.constants import *
from components.button import Button

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')

def read_settings():
   try:
       with open(SETTINGS, "r") as settings_file:
           settings = json.load(settings_file)
           return settings
   except FileNotFoundError:
       create_default_settings()
       return read_settings()

def update_algorithm(new_algorithm):
    settings = read_settings()
    settings["algorithm"] = new_algorithm
    with open(SETTINGS, "w") as settings_file:
        json.dump(settings, settings_file, indent=4)

def create_default_settings():
   default_settings = {"algorithm": ALGORITHMS[0]}
   with open(SETTINGS, "w") as settings_file:
       json.dump(default_settings, settings_file, indent=4)

def get_font(size, font):
    if font == "bold":
        return pygame.font.Font(BOLD_FONT, size)
    elif font == "regular":
        return pygame.font.Font(REGULAR_FONT, size)
    
def play(number=''):
    while True:
        WIN.blit(PRE_PLAY_BG, (0,0))
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_NUMBER = get_font(64, "bold").render(number, True, "Black")
        PLAY_NUMBER_RECT = PLAY_NUMBER.get_rect(center=(WIDTH/2, HEIGHT/2))
        WIN.blit(PLAY_NUMBER, PLAY_NUMBER_RECT)

        PLAY_BACK = Button(image=BACK_BTN, hover_image=BACK_BTN_H, pos=(64, 64))
        PLAY_PROCEED = Button(image=PROCEED_BTN_ACTIVE, hover_image=PROCEED_BTN_ACTIVE_H, pos=(WIDTH-64, HEIGHT-64), disabled_image=PROCEED_BTN_DISABLED, active=False)
        if number != '':
            if int(number) >= 8 and int(number) <= 18:
                PLAY_PROCEED = Button(image=PROCEED_BTN_ACTIVE, hover_image=PROCEED_BTN_ACTIVE_H, pos=(WIDTH-64, HEIGHT-64), disabled_image=PROCEED_BTN_DISABLED, active=True)
            
        for button in [PLAY_BACK,PLAY_PROCEED]:
            button.hover(PLAY_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    number = number[:-1]
                elif event.unicode.isdigit() and len(number) < 2:
                    number += event.unicode
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                    if PLAY_PROCEED.checkForInput(PLAY_MOUSE_POS):
                        pass
                        # game(algorithm)

            

        pygame.display.flip()
    
def options():
    settings = read_settings()
    algorithm = settings["algorithm"]

    while True:
        WIN.fill(WHITE)

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT_1 = get_font(32, "bold").render("CHOOSE ALGORITHM", True, "Black")
        OPTIONS_RECT_1 = OPTIONS_TEXT_1.get_rect(center=(WIDTH/2, HEIGHT*0.33))
        OPTIONS_TEXT_2 = get_font(24, "bold").render("OR", True, "Black")
        OPTIONS_RECT_2 = OPTIONS_TEXT_2.get_rect(center=(WIDTH*0.49, HEIGHT*0.3+78))

        WIN.blit(OPTIONS_TEXT_1, OPTIONS_RECT_1)
        WIN.blit(OPTIONS_TEXT_2, OPTIONS_RECT_2)

        OPTIONS_BACK = Button(image=BACK_BTN, hover_image=BACK_BTN_H, pos=(64, 64))
        MINIMAX_BUTTON = Button(image=MINIMAX_BTN, hover_image=MINIMAX_BTN_H, pos=(WIDTH*0.376, HEIGHT*0.3+78))
        ALPHABETA_BUTTON = Button(image=ALPHABETA_BTN, hover_image=ALPHABETA_BTN_H, pos=(WIDTH*0.614, HEIGHT*0.3+78))

        if algorithm == ALGORITHMS[0]:
            MINIMAX_BUTTON = Button(image=MINIMAX_BTN, hover_image=MINIMAX_BTN_H, pos=(WIDTH*0.376, HEIGHT*0.3+78), pressed=True)
        elif algorithm == ALGORITHMS[1]:
            ALPHABETA_BUTTON = Button(image=ALPHABETA_BTN, hover_image=ALPHABETA_BTN_H, pos=(WIDTH*0.614, HEIGHT*0.3+78), pressed=True)

        for button in [OPTIONS_BACK,MINIMAX_BUTTON,ALPHABETA_BUTTON]:
            button.hover(OPTIONS_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        update_algorithm(algorithm)
                        main_menu()
                    if MINIMAX_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                        algorithm = ALGORITHMS[0]
                    if ALPHABETA_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                        algorithm = ALGORITHMS[1]

        pygame.display.update()

def main_menu():
    while True:
        WIN.blit(MAIN_MENU_BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=PLAY_BTN, hover_image=PLAY_BTN_H, pos=(WIDTH/2, 286))
        OPTIONS_BUTTON = Button(image=OPTIONS_BTN, hover_image=OPTIONS_BTN_H, pos=(WIDTH/2, 358))
        QUIT_BUTTON = Button(image=QUIT_BTN, hover_image=QUIT_BTN_H, pos=(WIDTH/2, 430))

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.hover(MENU_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

        pygame.display.update()

main_menu()