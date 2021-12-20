from ast import literal_eval

LEAF = 'LEAF'; PAIR = 'PAIR'

leaf = lambda value: { 'type': LEAF, 'value': value, 'parent': None }
tree = lambda left, right: { 'type': PAIR, 'left': left, 'right': right, 'parent': None }
is_leaf = lambda _tree: _tree['type'] == LEAF
is_pair = lambda _tree: _tree['type'] == PAIR
magnitude = lambda _tree: _tree['value'] if is_leaf(_tree) else 3 * magnitude(_tree['left']) +  2 * magnitude(_tree['right'])
height = lambda _tree: 0 if is_leaf(_tree) else max(height(_tree['left']), height(_tree['right'])) + 1

def parse_literal_pair(val):
  if type(val) == list:
    left = parse_literal_pair(val[0])
    right = parse_literal_pair(val[1])
    _tree = tree(left, right)
    left['parent'] = _tree
    right['parent'] = _tree
    return _tree
  return leaf(val)

parse_tree = lambda str: parse_literal_pair(literal_eval(str))

def as_list(_tree):
  if (is_leaf(_tree)): return _tree['value']
  return [as_list(_tree['left']), as_list(_tree['right'])]

def any_literal_to_divide(_tree):
  if (is_leaf(_tree)): return _tree['value'] > 9
  return any_literal_to_divide(_tree['left']) or any_literal_to_divide(_tree['right'])

def replace_node(to_replace, new_tree):
  parent = to_replace['parent']
  if (parent['left'] == to_replace): parent['left'] = new_tree
  else: parent['right'] = new_tree
  new_tree['parent'] = parent

def find_to_divide(_tree):
  if(is_leaf(_tree) and _tree['value'] > 9): return _tree
  
  if(is_pair(_tree)):
    return find_to_divide(_tree['left']) or find_to_divide(_tree['right'])
  return None

def find_to_explode(_tree, level = 0):
  if (level == 4 and is_pair(_tree)): return _tree

  if(is_pair(_tree)):
    return find_to_explode(_tree['left'], level + 1) or find_to_explode(_tree['right'], level + 1)
  return None

def find_left_leaf(_tree, level = 0):
  if (_tree == None or _tree['parent'] == None): return None

  while (_tree['parent']['left'] == _tree):
    if (_tree['parent'] == None): return None
    _tree = _tree['parent']
    if (_tree['parent'] == None): return None
    level -= 1

  _tree = _tree['parent']['left']

  while (level < 0):
    if is_leaf(_tree): return _tree
    _tree = _tree['right']
    level += 1

  if (level == 0): return _tree

  return find_left_leaf(_tree, level)

def find_right_leaf(_tree, level = 0):
  if (_tree == None or _tree['parent'] == None): return None

  while (_tree['parent']['right'] == _tree):
    if (_tree['parent'] == None): return None
    _tree = _tree['parent']
    level -= 1

  _tree = _tree['parent']['right']

  while (level < 0):
    if is_leaf(_tree): return _tree
    _tree = _tree['left']
    level += 1

  if (level == 0): return _tree

  return find_right_leaf(_tree, level)