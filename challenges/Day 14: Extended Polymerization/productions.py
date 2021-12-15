input_path = 'advent_of_code_2021/challenges/Day 14: Extended Polymerization/test'
productions = {}
memoization = {}
steps = 10

def pairs(string):
  array = []; j = 0
  while (j+1 < len(string)):
    array.append(string[j:j+2]); j+=1
  return array

string = ''
count = {}

def produce_pattern(pattern, count):
  if (not pattern in productions): return pattern
  if (not productions[pattern] in count): count[productions[pattern]] = 0
  count[productions[pattern]] +=1
  return pattern[0] + productions[pattern] + pattern[1]

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