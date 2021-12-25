from functools import reduce
input_path = 'advent_of_code_2021/challenges/Day 3: Binary Diagnostic/input'

# Part 1
counter = [0 for i in range(12)]
num_by_bit = { '1': 1, '0': -1 }
numbers = []

with open(input_path) as f:
  for line in f:
    numbers.append(line)
    for i in range(12):
      counter[i] += num_by_bit[line[i]]

gamma_rate, epsilon_rate = reduce(lambda acc, elem: [
  acc[0] + ('1' if (elem > 0) else '0'),
  acc[1] + ('0' if (elem > 0) else '1'),
], counter, ['', ''])
print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# Part 2
def split_numbers(index, numbers):
  return reduce(lambda acc, binary:
  [
    acc[0] + num_by_bit[binary[index]],
    acc[1] + ([binary] if binary[index] == '1' else []),
    acc[2] + ([binary] if binary[index] == '0' else [])
  ],
  numbers, [0, [], []])

def winning_bit(count, priority):
  if (count == 0): return '1' if (priority == 'higher') else '0'
  return '1' if (count > 0 and priority == 'higher') or (count < 0 and priority == 'smaller') else '0'

def get_values(index, numbers, priority = 'higher'):
  if len(numbers) == 1: return numbers[0]
  count, with_one, with_zero = split_numbers(index, numbers)
  filtered = with_zero if winning_bit(count, priority) == '0' else with_one
  return get_values(index + 1, filtered, priority)

_, with_one, with_zero = split_numbers(0, numbers)
oxygen_generator_rating = get_values(1, with_zero, 'higher')
co2_scrubber_rating = get_values(1, with_one, 'smaller')

print(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))