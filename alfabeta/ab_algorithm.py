import math
from config.constants import MOVES
from copy import copy


def alphabeta(game, depth, alpha, beta, maximizing_player):
    if depth == 0:
        return game.evaluate_game(), None

    if maximizing_player:
        max_score = -math.inf
        best_move = None
        for move in MOVES:
            new_game = copy(game)
            new_game.make_move(move)
            score, _ = alphabeta(new_game, depth - 1, alpha, beta, False)
            if score is not None and score > max_score:
                max_score = score
                best_move = move
            alpha = max(alpha, max_score)
            if alpha >= beta:
                break
        return max_score, best_move
    else:
        min_score = math.inf
        best_move = None
        for move in MOVES:
            new_game = copy(game)
            new_game.make_move(move)
            score, _ = alphabeta(new_game, depth - 1, alpha, beta, True)
            if score is not None and score < min_score:
                min_score = score
                best_move = move
            beta = min(beta, min_score)
            if alpha >= beta:
                break
        return min_score, best_move
