import pygame
from config.constants import *

class Game:
    def __init__(self, win, number, turn):
        self.win = win
        self.number = number
        self.turn = turn
        self._init()

    def _init(self):
        self.score1 = SCORE1
        self.score2 = SCORE2
        self.bank = BANK

    def reset(self):
        self._init()

    def make_move(self, multiplier):
        self.number *= multiplier

        if self.number % 2 == 0:
            score = -1
        else:
            score = 1

        if str(self.number)[:-1] == '5' or str(self.number)[:-1] == '0':
            bank = 1

        self.change_turn()
        
        return self.turn, score, bank
    
    def check_number(self):
        if self.number % 2 == 0:
            score = -1
        else:
            score = 1
        if str(self.number)[:-1] == '5' or str(self.number)[:-1] == '0':
            bank = 1
        return self.turn, score, bank

    def change_turn(self):
        if self.turn == 'computer':
            self.turn = 'player'
        else:
            self.turn = 'computer'

    def get_state(self):
        return self.state
    
    def ai_move(self, state):
        self.state = state
        self.change_turn()