input_path = 'advent_of_code_2021/challenges/Day 18: Snailfish/test3'
from tree import tree, leaf, is_leaf, parse_tree, replace_node, find_to_explode, find_to_divide, any_literal_to_divide, find_right_leaf, find_left_leaf, as_list, height, magnitude

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
  replace_node(_leaf, tree(leaf(value//2), leaf(value//2 + (value % 2))))
  return _tree

def reduce(_tree):
  if (height(_tree) == 5): return reduce(explode_child(_tree))
  if (any_literal_to_divide(_tree)): return reduce(divide_child(_tree))
  return _tree

# with open(input_path) as f:
#   _tree = parse_tree(f.readline()[:-1])
#   for line in f: _tree = add(_tree, parse_tree(line[:-1]))
#   print(magnitude(_tree))

explode_child(parse_tree('[[[[5, 0], [[9, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]], [[[5, [2, 8]], 4], [5, [[9, 9], 0]]]]'))