import pygame
from config.constants import *

class Playground:
    def __init__(self, number, score1=SCORE1, score2=SCORE2, bank=BANK):
        self.number = number
        self.score1 = score1
        self.score2 = score2
        self.bank = bank

    def create_playground(self, win):
        pass