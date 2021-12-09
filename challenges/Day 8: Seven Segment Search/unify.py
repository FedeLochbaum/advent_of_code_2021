def digits(): return ['a', 'b', 'c', 'd', 'e', 'f', 'g']
def make_matrix(): return {
  'a': set(digits()), 'b': set(digits()), 'c': set(digits()),
  'd': set(digits()),
  'e': set(digits()), 'f': set(digits()), 'g': set(digits()),
}

number_by_digitis = { 'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9 }
easy_by_len = { 2: 'cf', 3: 'acf', 4: 'bcdf', 7: 'abcdefg' }
def is_easy(string): return len(string) in [2, 3, 4, 7]

def make_constraint_matrix(patterns):
  matrix = make_matrix()
  for pattern in patterns:
    pair = easy_by_len[len(pattern)]
    for char in pattern: matrix[char] = matrix[char].intersection(pair)
  return matrix

def sustitution_by(index): return lambda value: ''.join(sorted(map(lambda c: index[c], value)))

def is_valid_sustituion(sustitution, patterns):
  for value in patterns:
    if (not sustitution(value) in number_by_digitis): return False
  return True

def assignment(possible_assignments, patterns, stack, index):
  if(len(stack) == 0):
    sustitution = sustitution_by(index)
    return sustitution if is_valid_sustituion(sustitution, patterns) else None

  current = stack.pop()
  for assign in possible_assignments[current] - set(index.values()):
    index[current] = assign
    res = assignment(possible_assignments, patterns, stack, index)
    if (res != None): return res
    index[current] = None
  stack.insert(0, current)

def unify(patterns):
  trivials = list(filter(is_easy, patterns))
  return assignment(make_constraint_matrix(trivials), patterns, digits(), {})