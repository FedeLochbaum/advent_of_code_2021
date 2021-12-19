from collections import deque
from ast import literal_eval

LEAF = 'LEAF'
PAIR = 'PAIR'

leaf = lambda value, parent = None: { 'type': LEAF, 'value': value, 'height': 0, 'parent': parent }
tree = lambda left, right, parent = None: { 'type': PAIR, 'left': left, 'right': right, 'height': max(left['height'], right['height']) + 1, 'parent': parent }
is_leaf = lambda pair: pair['type'] == LEAF
is_pair = lambda pair: pair['type'] == PAIR

def parse_literal_pair(val):
  if type(val) == list:
    left = parse_literal_pair(val[0])
    right = parse_literal_pair(val[1])
    t = tree(left, right)
    left['parent'] = t
    right['parent'] = t
    return t
  return leaf(val)
parse_tree = lambda str: parse_literal_pair(literal_eval(str))

def as_list(t):
  if (is_leaf(t)): return t['value']
  return [as_list(t['left']), as_list(t['right'])]

def any_literal_to_divide(parent):
  if (is_leaf(parent)): return parent['value'] > 9
  return any_literal_to_divide(parent['left']) or any_literal_to_divide(parent['right'])

def replace_node(to_replace, new_tree):
  parent = to_replace['parent']
  new_tree['parent'] = parent
  if (parent['left'] == to_replace): parent['left'] = new_tree
  else: parent['right'] = new_tree
  parent['height'] = max(parent['left']['height'], parent['right']['height']) + 1

def find_to_divide(current):
  if(is_leaf(current) and current['value'] > 9): return current
  
  if(is_pair(current)):
    return find_to_divide(current['left']) or find_to_divide(current['right'])
  return None

def find_to_explode(parent, level = 0):
  if (level == 4 and is_pair(parent)): return parent

  if(is_pair(parent)):
    return find_to_explode(parent['left'], level + 1) or find_to_explode(parent['right'], level + 1)
  return None

def find_left_leaf(node, level = 0):
  if (node == None or node['parent'] == None): return None

  while (node['parent']['left'] == node or (node['parent']['left'] == None and node['parent']['right'] == node)):
    if (node['parent'] == None): return None

    node = node['parent']
    level -= 1

  node = node['parent']['left']

  while (level < 0):
    if (node['right'] != None): node = node['right']
    elif (node['left'] != None): node = node['left']
    else: break
    level += 1

  if (level == 0): return node

  return find_right_leaf(node, level)

def find_right_leaf(node, level = 0):
  if (node == None or node['parent'] == None): return None

  while (node['parent']['right'] == node or (node['parent']['right'] == None and node['parent']['left'] == node)):
    if (node['parent'] == None): return None

    node = node['parent']
    level -= 1

  node = node['parent']['right']

  while (level < 0):
    if (node['left'] != None): node = node['left']
    elif (node['right'] != None): node = node['right']
    else: break
    level += 1

  if (level == 0): return node    

  return find_right_leaf(node, level)