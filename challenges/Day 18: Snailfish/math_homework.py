input_path = 'advent_of_code_2021/challenges/Day 18: Snailfish/input'
from tree import tree, leaf, is_leaf, parse_tree, replace_node, find_to_explode, find_to_divide, any_literal_to_divide, find_right_leaf, find_left_leaf, height, magnitude

def add(pair1, pair2):
  _tree = tree(pair1, pair2)
  pair1['parent'] = _tree
  pair2['parent'] = _tree
  return reduce(_tree)

def explode_child(_tree):
  pair = find_to_explode(_tree)
  l_leaf = find_left_leaf(pair)
  r_leaf = find_right_leaf(pair, -1)
  if(l_leaf != None): l_leaf['value'] += pair['left']['value']
  if (r_leaf != None): r_leaf['value'] += pair['right']['value']
  replace_node(pair, leaf(0))
  return _tree

def divide_child(_tree):
  _leaf = find_to_divide(_tree)
  value = _leaf['value']
  _leaf1 = leaf(value//2)
  _leaf2 = leaf(value//2 + (value % 2))
  _new_tree = tree(_leaf1, _leaf2)
  _leaf1['parent'] = _new_tree
  _leaf2['parent'] = _new_tree
  replace_node(_leaf, _new_tree)
  return _tree

def reduce(_tree):
  if (height(_tree) == 5): return reduce(explode_child(_tree))
  if (any_literal_to_divide(_tree)): return reduce(divide_child(_tree))
  return _tree

with open(input_path) as f:
  _tree = parse_tree(f.readline()[:-1])
  for line in f:
    _tree = add(_tree, parse_tree(line[:-1]))
  print(magnitude(_tree))