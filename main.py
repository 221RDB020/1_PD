import json
import sys

from components.button import Button
from components.stroke import Stroke
from config.constants import *
from game.game import Game

pygame.init()

clock = pygame.time.Clock()

fps = 15

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('1. Praktiskais darbs')


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
    updated_settings = read_settings()


def create_default_settings():
    default_settings = {"algorithm": ALGORITHMS[0]}
    with open(SETTINGS, "w") as settings_file:
        json.dump(default_settings, settings_file, indent=4)


def get_font(size, font):
    if font == "bold":
        return pygame.font.Font(BOLD_FONT, size)
    elif font == "regular":
        return pygame.font.Font(REGULAR_FONT, size)


def run_game(number, game_starter):
    settings = read_settings()
    algorithm = settings["algorithm"]
    game = Game(WIN, number, game_starter)
    while True:
        WIN.blit(GAME_BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        number = game.number
        score1 = game.score1
        score2 = game.score2
        bank = game.bank

        if game.winner() in [-1, 0, 1]:
            winner = game.winner()
            if winner == 1:
                winner_text = "Dators uzvar!"
                score2 += bank
            elif winner == -1:
                winner_text = "Cilvēks uzvar!"
                score1 += bank
            else:
                winner_text = "Neizšķirts!"
            number = winner_text

        PLAY_BACK = Button(image=BACK_BTN, hover_image=BACK_BTN_H, pos=(56, 56))
        X2_BUTTON = Button(image=X2_BTN,
                           hover_image=X2_BTN_H,
                           pos=(WIDTH * 0.42, HEIGHT - 130))
        X3_BUTTON = Button(image=X3_BTN,
                           hover_image=X3_BTN_H,
                           pos=(WIDTH / 2, HEIGHT - 130))
        X4_BUTTON = Button(image=X4_BTN,
                           hover_image=X4_BTN_H,
                           pos=(WIDTH * 0.58, HEIGHT - 130))

        NUMBER_TXT = Stroke(number, "bold", 96, 3, WHITE, BLACK,
                            (WIDTH / 2, HEIGHT / 2))
        NUMBER_TXT_SHADOW = Stroke(number, "bold", 96, 3, BLACK, BLACK,
                                   (WIDTH / 2, HEIGHT / 2 + 4))

        SCORE1_TXT = Stroke(str(score1), "bold", 24, 3, BLACK, WHITE,
                            (WIDTH * 0.282, HEIGHT - 45))
        SCORE2_TXT = Stroke(str(score2), "bold", 24, 3, BLACK, WHITE,
                            (WIDTH * 0.716, HEIGHT - 45))

        BANK_TEXT = get_font(24, "bold").render(str(bank), True, BLACK)
        BANK_RECT = BANK_TEXT.get_rect(center=(WIDTH - 49, 40))

        WIN.blit(BANK_TEXT, BANK_RECT)

        for button in [PLAY_BACK, X2_BUTTON, X3_BUTTON, X4_BUTTON]:
            button.hover(PLAY_MOUSE_POS)
            button.update(WIN)

        for text in [NUMBER_TXT_SHADOW, NUMBER_TXT, SCORE1_TXT, SCORE2_TXT]:
            text.render(WIN)

        if game.winner() not in [-1, 0, 1]:
            if game.turn == 'computer':
                game.ai_move(game.get_state(), algorithm, 4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        play()
                    if game.winner() not in [-1, 0, 1]:
                        if game.turn == 'player':
                            if X2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                                game.make_move(2)
                            elif X3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                                game.make_move(3)
                            elif X4_BUTTON.checkForInput(PLAY_MOUSE_POS):
                                game.make_move(4)

        pygame.display.update()

        clock.tick(fps)


def play():
    global number, game_starter
    number = game_starter = ''
    while True:
        WIN.blit(PRE_PLAY_BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_NUMBER = get_font(64, "bold")
        if PLAY_NUMBER is not None:
            PLAY_NUMBER = PLAY_NUMBER.render(number, True, "Black")
            PLAY_NUMBER_RECT = PLAY_NUMBER.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            WIN.blit(PLAY_NUMBER, PLAY_NUMBER_RECT)
        PLAY_BACK = Button(image=BACK_BTN, hover_image=BACK_BTN_H, pos=(56, 56))
        PLAY_PROCEED = Button(image=PROCEED_BTN_ACTIVE,
                              hover_image=PROCEED_BTN_ACTIVE_H,
                              pos=(WIDTH - 56, HEIGHT - 56),
                              disabled_image=PROCEED_BTN_DISABLED,
                              active=False)
        PERSON_BUTTON = Button(image=PERSON_BTN,
                               hover_image=PERSON_BTN_H,
                               pos=(WIDTH - 48, HEIGHT - 224))
        COMPUTER_BUTTON = Button(image=COMPUTER_BTN,
                                 hover_image=COMPUTER_BTN_H,
                                 pos=(WIDTH - 48, HEIGHT - 144))
        if game_starter == 'player':
            PERSON_BUTTON = Button(image=PERSON_BTN,
                                   hover_image=PERSON_BTN_H,
                                   pos=(WIDTH - 48, HEIGHT - 224),
                                   pressed=True)
        elif game_starter == 'computer':
            COMPUTER_BUTTON = Button(image=COMPUTER_BTN,
                                     hover_image=COMPUTER_BTN_H,
                                     pos=(WIDTH - 48, HEIGHT - 144),
                                     pressed=True)
        if number != '' and game_starter != '':
            if int(number) >= 8 and int(number) <= 18:
                PLAY_PROCEED = Button(image=PROCEED_BTN_ACTIVE,
                                      hover_image=PROCEED_BTN_ACTIVE_H,
                                      pos=(WIDTH - 56, HEIGHT - 56),
                                      disabled_image=PROCEED_BTN_DISABLED,
                                      active=True)

        for button in [PLAY_BACK, PLAY_PROCEED, PERSON_BUTTON, COMPUTER_BUTTON]:
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
                        run_game(number, game_starter)
                    if PERSON_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        game_starter = 'player'
                    if COMPUTER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        game_starter = 'computer'

        pygame.display.flip()


def options():
    settings = read_settings()
    algorithm = settings["algorithm"]
    while True:
        WIN.fill(WHITE)

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT_1 = get_font(32, "bold")
        if OPTIONS_TEXT_1 is not None:
            OPTIONS_TEXT_1 = OPTIONS_TEXT_1.render("CHOOSE ALGORITHM", True, BLACK)
            OPTIONS_RECT_1 = OPTIONS_TEXT_1.get_rect(center=(WIDTH / 2,
                                                             HEIGHT * 0.33))
            WIN.blit(OPTIONS_TEXT_1, OPTIONS_RECT_1)
        OPTIONS_TEXT_2 = get_font(24, "bold")
        if OPTIONS_TEXT_2 is not None:
            OPTIONS_TEXT_2 = OPTIONS_TEXT_2.render("OR", True, BLACK)
            OPTIONS_RECT_2 = OPTIONS_TEXT_2.get_rect(center=(WIDTH * 0.49,
                                                             HEIGHT * 0.3 + 78))
            WIN.blit(OPTIONS_TEXT_2, OPTIONS_RECT_2)

        OPTIONS_BACK = Button(image=BACK_BTN, hover_image=BACK_BTN_H, pos=(56, 56))
        MINIMAX_BUTTON = Button(image=MINIMAX_BTN,
                                hover_image=MINIMAX_BTN_H,
                                pos=(WIDTH * 0.376, HEIGHT * 0.3 + 78))
        ALPHABETA_BUTTON = Button(image=ALPHABETA_BTN,
                                  hover_image=ALPHABETA_BTN_H,
                                  pos=(WIDTH * 0.614, HEIGHT * 0.3 + 78))

        if algorithm == ALGORITHMS[0]:
            MINIMAX_BUTTON = Button(image=MINIMAX_BTN,
                                    hover_image=MINIMAX_BTN_H,
                                    pos=(WIDTH * 0.376, HEIGHT * 0.3 + 78),
                                    pressed=True)
        elif algorithm == ALGORITHMS[1]:
            ALPHABETA_BUTTON = Button(image=ALPHABETA_BTN,
                                      hover_image=ALPHABETA_BTN_H,
                                      pos=(WIDTH * 0.614, HEIGHT * 0.3 + 78),
                                      pressed=True)

        for button in [OPTIONS_BACK, MINIMAX_BUTTON, ALPHABETA_BUTTON]:
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
        WIN.blit(MAIN_MENU_BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=PLAY_BTN,
                             hover_image=PLAY_BTN_H,
                             pos=(WIDTH / 2, 286))
        OPTIONS_BUTTON = Button(image=OPTIONS_BTN,
                                hover_image=OPTIONS_BTN_H,
                                pos=(WIDTH / 2, 358))
        QUIT_BUTTON = Button(image=QUIT_BTN,
                             hover_image=QUIT_BTN_H,
                             pos=(WIDTH / 2, 430))

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
