input_path = 'advent_of_code_2021/challenges/Day 18: Snailfish/test1'
from tree import tree, leaf, is_leaf, parse_tree, replace_node, find_to_explode, find_to_divide, any_literal_to_divide, find_right_leaf, find_left_leaf, as_list, height

magnitude = lambda pair: pair['value'] if is_leaf(pair) else 3 * magnitude(pair['left']) +  2 * magnitude(pair['right'])

def add(pair1, pair2):
  t = tree(pair1, pair2)
  pair1['parent'] = t
  pair2['parent'] = t
  return reduce(t)

def explode_child(parent):
  p = find_to_explode(parent)
  left = p['left']
  right = p['right']
  l_leaf = find_left_leaf(p, 0)
  r_leaf = find_right_leaf(p, 0)

  replace_node(p, leaf(0))
  if(l_leaf != None): l_leaf['value'] += left['value']
  if (r_leaf != None): r_leaf['value'] += right['value']

  return parent

def divide_child(_tree):
  l = find_to_divide(_tree)
  value = l['value']
  replace_node(l, tree(
    leaf(value//2),
    leaf(value//2 + (1 if value % 2 == 1 else 0))
  ))

  return _tree

def reduce(pair):
  print('reduce: ', as_list(pair))
  if (height(pair) == 5):
    return reduce(explode_child(pair))
  if (any_literal_to_divide(pair)): return reduce(divide_child(pair))
  return pair

# with open(input_path) as f:
#   current = parse_tree(f.readline()[:-1])
#   for line in f: current = add(current, parse_tree(line[:-1]))
#   print(magnitude(current))


reduce(parse_tree('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'))