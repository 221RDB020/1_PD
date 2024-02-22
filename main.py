import pygame, sys
from config.constants import WIDTH, HEIGHT, WHITE, REGULAR_FONT, BOLD_FONT, MAIN_MENU_BG, PLAY_BTN, PLAY_BTN_H, OPTIONS_BTN, OPTIONS_BTN_H, QUIT_BTN, QUIT_BTN_H, BACK_BTN, BACK_BTN_H
from components.button import Button

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')

def get_font(size, font):
    if font == "bold":
        return pygame.font.Font(BOLD_FONT, size)
    elif font == "regular":
        return pygame.font.Font(REGULAR_FONT, size)
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        WIN.fill(WHITE)

        OPTIONS_TEXT = get_font(45, "bold").render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        WIN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=BACK_BTN, hover_image=BACK_BTN_H, pos=(64, 64))

        OPTIONS_BACK.hover(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                    # play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()