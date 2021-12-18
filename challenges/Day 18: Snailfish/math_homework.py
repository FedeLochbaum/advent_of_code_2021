input_path = 'advent_of_code_2021/challenges/Day 18: Snailfish/test0'
from ast import literal_eval
from collections import deque

LEAF = 'LEAF'
PAIR = 'PAIR'

literal = lambda value: { 'type': LEAF, 'value': value, 'height': 0 }
pair = lambda left, right: { 'type': PAIR, 'left': left, 'right': right, 'height': max(left['height'], right['height']) + 1 }
is_leaf = lambda pair: pair['type'] == LEAF
is_pair = lambda pair: pair['type'] == PAIR

def any_literal_to_divide(parent):
  if (is_leaf(parent)): return parent['value'] > 9
  return any_literal_to_divide(parent['left']) or any_literal_to_divide(parent['right'])

def update_by_path(parent, path, new_value):
  queue = deque(path)
  current = parent
  if len(path) == 0: return
  while(len(path) > 1):
    index = queue.popleft()
    current = current['left' if index == 0 else 'right']
  last = queue.popleft()
  current['left' if last == 0 else 'right'] = new_value

def find_by_root(parent, found, path = []):
  if (found(parent, path)): return path, parent
  left_path, l_child = find_by_root(parent['left'], found, path + [0])
  if (left_path != None): return left_path, l_child
  right_path, r_child = find_by_root(parent['right'], found, path + [1])
  if (right_path != None): return [right_path, r_child]
  return [None, None]

# TODO: re think
# def find_first_to_left_from(parent, path):
  # if (path[-1] == 0):


def find_by_leaf(child, found, path):
  if (found(child, path)): return path, child
  # if(path[-1] == 0) # 



  # left_path, l_child = find_by_root(parent['left'], found, path + [0])
  # if (left_path != None): return left_path, l_child
  # right_path, r_child = find_by_root(parent['right'], found, path + [1])
  # if (right_path != None): return [right_path, r_child]
  # return [None, None]

find_child_to_divide_path = lambda parent: find_by_root(parent, lambda node, _: is_leaf(node) and node['value'] > 9)
find_explode_path = lambda parent: find_by_root(parent, lambda node, current_path: len(current_path) == 3 and is_pair(node))

find_first_to_left_from = lambda parent: find_by_leaf(parent, lambda node, current_path: is_leaf(node) and current_path[-1] == 0)
find_first_to_right_from = lambda parent: find_by_leaf(parent, lambda node, current_path: is_leaf(node) and current_path[-1] == 1)

def explode_child(parent):
  path, p = find_explode_path(parent)
  left = p['left']
  right = p['right']
  update_by_path(parent, path, literal(0))
  left_path, l_leaf = find_first_to_left_from(parent, path)
  right_path, r_leaf = find_first_to_right_from(parent, path)
  if(left_path != None): update_by_path(parent, left_path, literal(l_leaf['value'] + left['value']))
  if (right_path != None): update_by_path(parent, right_path, literal(r_leaf['value'] + right['value']))
  return parent

def divide_child(parent):
  path, leaf = find_child_to_divide_path(parent)
  update_by_path(parent, path, pair(
    literal(leaf//2),
    literal(leaf//2 + (1 if leaf % 2 == 1 else 0))
  ))
  return parent

def reduce(pair):
  if (pair['height'] == 4): return reduce(explode_child(pair))
  if (any_literal_to_divide(pair)): return reduce(divide_child(pair))
  return pair

magnitude = lambda pair: pair['value'] if is_leaf(pair) else 3 * magnitude(pair['left']) +  2 * magnitude(pair['right'])
add = lambda pair1, pair2: reduce(pair(pair1, pair2))

parse_literal_pair = lambda val: pair(parse_literal_pair(val[0]), parse_literal_pair(val[1])) if type(val) == list else literal(val)
parse_pair = lambda str: parse_literal_pair(literal_eval(str))

with open(input_path) as f:
  current = parse_pair(f.readline()[:-1])
  for line in f:
    current = add(current, parse_pair(line[:-1]))
  print(magnitude(current))