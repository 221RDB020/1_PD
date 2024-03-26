from copy import copy
from config.constants import MOVES


def minimax(position, depth, max_player, game):
  if depth == 0:
    return game.evaluate_game(), position

  if max_player:
    maxEval = float('-inf')
    best_move = None
    for move in MOVES:
      new_game = copy(game)
      evaluation = minimax(move, depth - 1, False, new_game)[0]
      maxEval = max(maxEval, int(evaluation))
      if maxEval == evaluation:
        best_move = move
    #print ("bestmove: ",best_move, "max: ",maxEval)
    return maxEval, best_move
  else:
    minEval = float('inf')
    best_move = None
    for move in MOVES:
      new_game = copy(game)
      evaluation = minimax(move, depth - 1, True, new_game)[0]
      minEval = min(minEval, int(evaluation))
      if minEval == evaluation:
        best_move = move
    #print ("bestmove: ",best_move, "min: ",minEval)
    return minEval, best_move


# def animate_moves(game, playground, multiplier):
#   playground.draw(game.win)
#   pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
#   pygame.display.update()
