import math
import time
from config.constants import *
from minimax.algorithm import minimax
from alfabeta.ab_algorithm import alphabeta
from game.gameTree import GameTreeNode, GameTree, generate_game_tree


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
    game_tree = GameTree(self.number)
    generate_game_tree(game_tree.root, depth, 0)
    if algorithm == ALGORITHMS[0]:
      number, best_move = minimax(game_tree.root, depth, True,self)  #position, depth, max_player, game
    else:
      score, best_move = alphabeta(self, depth, -math.inf, math.inf, True)
    self.make_move(best_move)

  def evaluate_game(self):
    if int(self.number) >= 1200:
      if self.score2 + self.bank > self.score1:
        return 1  #dators uzvar
      elif self.score2 + self.bank < self.score1:
        return -1  #cilveks uzvar
      else:
        return 0  #neizskirts
    else:
      return float(self.number)  #spele nav beigusies
