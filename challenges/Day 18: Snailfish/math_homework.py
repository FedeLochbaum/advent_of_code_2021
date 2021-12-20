input_path = 'advent_of_code_2021/challenges/Day 18: Snailfish/input'
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

numbers = []
with open(input_path) as f:
  first_line = f.readline()[:-1]
  _tree = parse_tree(first_line)
  numbers.append(first_line)
  for line in f:
    numbers.append(line[:-1])
    _tree = add(_tree, parse_tree(line[:-1]))
  # part 1
  print(magnitude(_tree))

# Part 2
_max = 0
for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    first_magnitude = magnitude(add(parse_tree(numbers[i]), parse_tree(numbers[j])))
    second_magnitude = magnitude(add(parse_tree(numbers[j]), parse_tree(numbers[i])))
    _max = max(_max, max(first_magnitude, second_magnitude))
print(_max)