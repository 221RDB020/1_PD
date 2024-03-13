import pygame

WIDTH, HEIGHT = 1000, 565

WHITE = (255,255,255)
BLACK = (0,0,0)

SETTINGS = 'config/settings.json'

ALGORITHMS = ['mini-max','alpha-beta']

MOVES = [2,3,4]

SCORE1 = 0
SCORE2 = 0

BANK = 0

REGULAR_FONT = 'assets/fonts/fontRegular.ttf'
BOLD_FONT = 'assets/fonts/fontBold.ttf'

MAIN_MENU_BG = pygame.image.load("assets/images/main_menu_bg.png")
PRE_PLAY_BG = pygame.image.load("assets/images/pre_play_bg.png")
GAME_BG = pygame.image.load("assets/images/game_bg.png")
PLAY_BTN = pygame.image.load("assets/images/play_btn.png")
PLAY_BTN_H = pygame.image.load("assets/images/play_btn_h.png")
PROCEED_BTN_DISABLED = pygame.image.load("assets/images/proceed_disabled.png")
PROCEED_BTN_ACTIVE = pygame.image.load("assets/images/proceed_active.png")
PROCEED_BTN_ACTIVE_H = pygame.image.load("assets/images/proceed_active_h.png")
OPTIONS_BTN = pygame.image.load("assets/images/options_btn.png")
OPTIONS_BTN_H = pygame.image.load("assets/images/options_btn_h.png")
QUIT_BTN = pygame.image.load("assets/images/quit_btn.png")
QUIT_BTN_H = pygame.image.load("assets/images/quit_btn_h.png")
BACK_BTN = pygame.image.load("assets/images/back_btn.png")
BACK_BTN_H = pygame.image.load("assets/images/back_btn_h.png")
MINIMAX_BTN = pygame.image.load("assets/images/minimax_btn.png")
MINIMAX_BTN_H = pygame.image.load("assets/images/minimax_btn_h.png")
ALPHABETA_BTN = pygame.image.load("assets/images/alphabeta_btn.png")
ALPHABETA_BTN_H = pygame.image.load("assets/images/alphabeta_btn_h.png")
PERSON_BTN = pygame.image.load("assets/images/person_btn.png")
PERSON_BTN_H = pygame.image.load("assets/images/person_btn_h.png")
COMPUTER_BTN = pygame.image.load("assets/images/computer_btn.png")
COMPUTER_BTN_H = pygame.image.load("assets/images/computer_btn_h.png")
X2_BTN = pygame.image.load("assets/images/x2_btn.png")
X2_BTN_H = pygame.image.load("assets/images/x2_btn_h.png")
X3_BTN = pygame.image.load("assets/images/x3_btn.png")
X3_BTN_H = pygame.image.load("assets/images/x3_btn_h.png")
X4_BTN = pygame.image.load("assets/images/x4_btn.png")
X4_BTN_H = pygame.image.load("assets/images/x4_btn_h.png")