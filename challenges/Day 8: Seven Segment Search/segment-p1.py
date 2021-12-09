input_path = 'advent_of_code_2021/challenges/Day 8: Seven Segment Search/input'

# Part 1
easy_digits_count = 0

with open(input_path) as f:
  for line in f:
    _, values = line.split(' | ')
    for value in values[:-1].split(' '): easy_digits_count += (1 if len(value) in [2, 3, 4, 7] else 0)
print(easy_digits_count)
