import pygame

WIDTH, HEIGHT = 1000, 565

WHITE = (255,255,255)
BLACK = (0,0,0)

STARTING_NUMBER = 8
MOVES = [2,3,4]

SCORE1 = 0
SCORE2 = 0

BANK = 0

REGULAR_FONT = 'assets/fonts/fontRegular.ttf'
BOLD_FONT = 'assets/fonts/fontBold.ttf'

MAIN_MENU_BG = pygame.image.load("assets/images/main_menu_bg.png")
PLAY_BTN = pygame.image.load("assets/images/play_btn.png")
PLAY_BTN_H = pygame.image.load("assets/images/play_btn_h.png")
OPTIONS_BTN = pygame.image.load("assets/images/options_btn.png")
OPTIONS_BTN_H = pygame.image.load("assets/images/options_btn_h.png")
QUIT_BTN = pygame.image.load("assets/images/quit_btn.png")
QUIT_BTN_H = pygame.image.load("assets/images/quit_btn_h.png")
BACK_BTN = pygame.image.load("assets/images/back_btn.png")
BACK_BTN_H = pygame.image.load("assets/images/back_btn_h.png")