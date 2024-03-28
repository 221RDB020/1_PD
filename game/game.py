import math

from alfabeta.ab_algorithm import alphabeta
from config.constants import *
from minimax.algorithm import minimax


class Game:

    def __init__(self, win, number, turn):
        self.win = win
        self.number = number
        self.turn = turn
        self.state = None
        self._init()

    def _init(self):
        self.score1 = SCORE1
        self.score2 = SCORE2
        self.bank = BANK

    def reset(self):
        self._init()

    def make_move(self, multiplier):
        self.number = int(self.number) * multiplier
        turn, score, bank = self.check_number()

        if turn == 'player':
            self.score1 += score
        else:
            self.score2 += score

        self.bank += bank
        self.state = (self.number, self.score1, self.score2, self.bank, self.turn)
        if int(self.number) <= 1200:
            self.change_turn()

    def check_number(self):
        bank = 0
        score = -1 if int(self.number) % 2 == 0 else 1
        if str(self.number)[-1] == '5' or str(self.number)[-1] == '0':
            bank = 1
        return self.turn, score, bank

    def change_turn(self):
        if self.turn == 'computer':
            self.turn = 'player'
        else:
            self.turn = 'computer'

    def get_state(self):
        return self.state

    def ai_move(self, state, algorithm, depth):
        self.state = state
        if algorithm == ALGORITHMS[0]:
            score, best_move = minimax(self, depth, True)
        else:
            score, best_move = alphabeta(self, depth, -math.inf, math.inf, True)
        self.make_move(best_move)

    def winner(self):
        if int(self.number) >= 1200:
            if self.turn == 'computer':
                self.score2 += self.bank
                self.bank = 0
                if self.score2 > self.score1:
                    return 1  # dators uzvar
                elif self.score2 < self.score1:
                    return -1  # cilveks uzvar
                else:
                    return 0  # neizskirts
            else:
                self.score1 += self.bank
                self.bank = 0
                if self.score2 > self.score1:
                    return 1  # dators uzvar
                elif self.score2 < self.score1:
                    return -1  # cilveks uzvar
                else:
                    return 0  # neizskirts

    def evaluate_moves(self):
        f1 = -1 if int(self.number) % 2 == 0 else 1
        f2 = 1 if str(self.number)[-1] in ['0', '5'] else 0
        f4 = 0
        f5 = 10 if self.score1 == self.score2 and int(self.number >= 1200) else 0
        
        if self.turn == 'computer':
            f3 = self.score2 - self.score1

            if self.score2 + self.bank > self.score1:
                f4 = 9999 if int(self.number) >= 1200 else 0
        else:
            f3 = self.score1 - self.score2

            if self.score1 + self.bank > self.score2:
                f4 = -9999 if int(self.number) >= 1200 else 0

        score = f1 + f2 + f3 + f4 + f5
        print(f"turn: {self.turn} score1: {self.score1} score2: {self.score2} number: {self.number} f1: {f1} f2: {f2} f3: {f3} f4: {f4} score: {score}")
        return score
