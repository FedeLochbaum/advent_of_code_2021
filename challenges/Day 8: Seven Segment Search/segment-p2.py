input_path = 'advent_of_code_2021/challenges/Day 8: Seven Segment Search/input'
from unify import unify, number_by_digitis

with open(input_path) as f:
  sum = 0
  for line in f:
    patterns, values = line[:-1].split(' | ')
    sustitution = unify(patterns.split(' '))
    pattern_value = 0
    values = values.split(' ')
    for i, value in enumerate(values):
      pattern_value += number_by_digitis[sustitution(value)] * 10**(len(values) - i - 1)
    sum += pattern_value
print(sum)