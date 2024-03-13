class GameTree:
  def __init__(self, current_number):
    self.current_number = current_number


def generate_game_tree(current_number, max_depth, current_depth, score):
  if current_depth >= max_depth:
    return

  print("Depth:", current_depth)
  print("Current Number:", current_number)
  print("Current Score:", score)
  print("")

  next_numbers = [current_number * i for i in [2, 3, 4]]

  for number in next_numbers:
    new_number = number

    generate_game_tree(new_number, max_depth, current_depth + 1, score + evaluate(current_number))

def evaluate(current_number):
    score = 0
    game_bank = 0
    if current_number % 2 == 0:
        score -= 1
    else:
        score += 1

    last_digit = str(current_number)[-1]

    if last_digit == '0' or last_digit == '5':
        game_bank += 1
    
    return score + (0.5 * game_bank)
    

choosed_number = 13
max_depth = 5
generate_game_tree(choosed_number, max_depth, 0, 0)