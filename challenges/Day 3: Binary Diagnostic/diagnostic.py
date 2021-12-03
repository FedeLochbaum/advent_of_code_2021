from functools import reduce  
input_path = 'advent_of_code_2021/challenges/Day 3: Binary Diagnostic/input'

# Part 1
counter = [0 for i in range(12)]
num_by_bit = { '1': 1, '0': -1 }

with open(input_path) as f:
  for line in f:
    for i in range(12):
      counter[i] += num_by_bit[line[i]]
  gamma_rate, epsilon_rate = reduce(lambda a,e: [
    a[0] + ('1' if (e > 0) else '0'),
    a[1] + ('0' if (e > 0) else '1'),
  ], counter, ['', ''])
  print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# Part 2