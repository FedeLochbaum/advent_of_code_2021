input_path = 'advent_of_code_2021/challenges/Day 14: Extended Polymerization/test'
productions = {}
count = {}
memoization = {} # sub_string => counts
string = []
steps = 25
def add_at_index(str, index, replacement=''): return '%s%s%s'%(str[:index], replacement, str[index:])

def pairs(string):
  array = []; j = 0
  while (j+1 < len(string)):
    array.append(string[j:j+2]); j+=1
  return array

def step_pattern(pattern):
  if (pattern in productions):
    char = productions[pattern]
    return { char: 1 }, pattern[0] + char + pattern[1]

def prod_and_count_pairs(patterns, steps):
  count = {}
  if (steps > 0):
    for pattern in patterns:
      _count, sub_string = memoization[pattern] if pattern in memoization else step_pattern(pattern)
      __count = prod_and_count(sub_string, steps-1)
      for char in _count: count[char] = _count[char] + (count[char] if char in count else 0)
      for char in __count: count[char] = __count[char] + (count[char] if char in count else 0)
  return count

def prod_and_count(_string, steps):
  return prod_and_count_pairs(pairs(_string), steps)
    
with open(input_path) as f:
  for i, line in enumerate(f):
    if i == 0:
      for char in line[:-1]: count[char] = count[char] + 1 if char in count else 1
      string = line[:-1]
    if (i > 1):
      pattern, production = line[:-1].split(' -> ')
      productions[pattern] = production

_count = prod_and_count(string, steps)
for char in _count: count[char] = _count[char] + (count[char] if char in count else 0)

print(count)