import pygame
from config.constants import WHITE, BLACK
from playground import Playground

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.playground.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.playground = Playground()
        self.turn = "player_1"

    def winner(self):
        return self.playground.winner()
    
    def reset(self):
        self._init()

    def select(self, multiplier):
        if self.selected:
            result = self._move(multiplier)
            if not result:
                self.selected = None
                self.select(multiplier)
    
    def change_turn(self):
        if self.turn == "player_1":
            self.turn = "player_2"
        else:
            self.turn = "player_1"
    
    def get_playground(self):
        return self.board
    
    def ai_move(self, playground):
        self.playground = playground
        self.change_turn()