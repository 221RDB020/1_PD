class GameTreeNode:

  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    self.children.append(child_node)

  def get_children(self):
    return self.children

  def is_leaf(self):
    return len(self.children) == 0

class GameTree:

  def __init__(self, root_value):
    self.root = GameTreeNode(root_value)

  def add_child_to_root(self, child_value):
    child_node = GameTreeNode(child_value)
    self.root.add_child(child_node)


def generate_game_tree(current_node, max_depth, current_depth):
  if current_depth >= max_depth:
    return

  possible_moves = [2, 3, 4]

  for move in possible_moves:
    child_value = current_node.value * move
    child_node = GameTreeNode(child_value)
    current_node.add_child(child_node)
    generate_game_tree(child_node, max_depth, current_depth + 1)
