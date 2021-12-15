input_path = 'advent_of_code_2021/challenges/Day 14: Extended Polymerization/input'
from collections import deque
productions = {}
memoization = {}
pairs_memo = {}
steps = 30

def pairs(string):
  if not string in pairs_memo:
    array = []; j = 0
    while (j+1 < len(string)):
      array.append(string[j:j+2]); j+=1
    pairs_memo[string] = array
  return pairs_memo[string]

string = ''
count = {}

def produce_pattern(pattern, count):
  if (not pattern in productions): return pattern
  if (not productions[pattern] in count): count[productions[pattern]] = 0
  count[productions[pattern]] +=1
  return pattern[0] + productions[pattern] + pattern[1]

def step(string):
  if(not string in memoization):
    _count = {}
    sub_strings = list(map(lambda pattern: produce_pattern(pattern, _count), pairs(string)))
    memoization[string] = _count, sub_strings

  __count, sub_strings = memoization[string]
  for char in __count: count[char] = __count[char] + (count[char] if char in count else 0)
  return sub_strings

def produce(s, steps):
  next = deque()
  next.append(s)
  for i in range(steps):
    print(i)
    queue = next
    next = deque()
    while(queue):
      current = queue.popleft()
      sub_strings = step(current)
      for sub_string in sub_strings:
        next.append(sub_string)

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