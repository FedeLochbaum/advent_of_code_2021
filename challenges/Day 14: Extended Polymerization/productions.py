input_path = 'advent_of_code_2021/challenges/Day 14: Extended Polymerization/input'
productions = {}
steps = 40

def pairs(string):
  array = []; j = 0
  while (j+1 < len(string)):
    array.append(string[j:j+2]); j+=1
  return array

indexed_pairs = {}
count = {}
def produce(steps, indexed_pairs):
  for _ in range(steps):
    copied = indexed_pairs.copy()
    for pattern in indexed_pairs:
      a, b = pattern
      n = indexed_pairs[pattern]
      if (n > 0 and pattern in productions):
        char = productions[pattern]
        copied[pattern] -= n
        if (not a + char in copied): copied[a + char] = 0
        if (not char + b in copied): copied[char + b] = 0
        if (not char in count): count[char] = 0
        copied[a + char] += n
        copied[char + b] += n
        count[char] += n
    indexed_pairs = copied
  return indexed_pairs

with open(input_path) as f:
  for i, line in enumerate(f):
    if i == 0:
      for char in line[:-1]: count[char] = count[char] + 1 if char in count else 1
      for pair in pairs(line[:-1]):
        if (not pair in indexed_pairs): indexed_pairs[pair] = 0
        indexed_pairs[pair] += 1
    if (i > 1):
      pattern, production = line[:-1].split(' -> ')
      productions[pattern] = production

produce(steps, indexed_pairs)
print(max(count.values()) - min(count.values()))