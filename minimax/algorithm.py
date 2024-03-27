from copy import copy
from config.constants import MOVES


def minimax(game, depth, maximizing_player):
    if depth == 0 or game.winner() is not None:
        return game.evaluate_moves(), None

    if maximizing_player:
        max_score = float('-inf')
        best_move = None
        for move in MOVES:
            new_game = copy(game)
            new_game.make_move(move)
            score, _ = minimax(new_game, depth - 1, False)
            max_score = max(max_score, score)
            if max_score == score:
                best_move = move
        return max_score, best_move
    else:
        min_score = float('inf')
        best_move = None
        for move in MOVES:
            new_game = copy(game)
            new_game.make_move(move)
            score, _ = minimax(new_game, depth - 1, True)
            min_score = min(min_score, score)
            if min_score == score:
                best_move = move
        return min_score, best_move

