input_path = 'advent_of_code_2021/challenges/Day 14: Extended Polymerization/test'
productions = {}
memoization = {} # sub_string => counts
steps = 10
def add_at_index(str, index, replacement=''): return '%s%s%s'%(str[:index], replacement, str[index:])

def pairs(string):
  array = []; j = 0
  while (j+1 < len(string)):
    array.append(string[j:j+2]); j+=1
  return array

string = ''
count = {}

def produce_pattern(pattern, count):
  if (not pattern in memoization):
    if (pattern in productions):
      char = productions[pattern]
      memoization[pattern] = { char: 1 }, pattern[0] + char + pattern[1]
  
  if (not pattern in productions): return pattern

  _count, s = memoization[pattern]
  for char in _count: count[char] = _count[char] + (count[char] if char in count else 0)
  return s

def produce(string, steps):
  if (steps == 0): return
  if(string in memoization):
    _count, sub_strings = memoization[string]
    for char in _count: count[char] = _count[char] + (count[char] if char in count else 0)
    for sub_string in sub_strings: produce(sub_string, steps - 1)
  else:
    _count = {}
    sub_strings = list(map(lambda pattern: produce_pattern(pattern, _count), pairs(string)))
    memoization[string] = _count, sub_strings
    for char in _count: count[char] = _count[char] + (count[char] if char in count else 0)
    for sub_string in sub_strings: produce(sub_string, steps - 1)

with open(input_path) as f:
  for i, line in enumerate(f):
    if i == 0:
      for char in line[:-1]: count[char] = count[char] + 1 if char in count else 1
      string = line[:-1]
    if (i > 1):
      pattern, production = line[:-1].split(' -> ')
      productions[pattern] = production

produce(string, steps)
print(count)
# print(memoization)