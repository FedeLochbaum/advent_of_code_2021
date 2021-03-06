from functools import reduce
input_path = 'advent_of_code_2021/challenges/Day 6: Lanternfish/input'

memoization = { 0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {} }

def fishes_in_days(days, n):
  time = n - (days + 1)
  if (n == 0 or time < 0): return 0
  if (n in memoization[days]): return memoization[days][n]
  memoization[days][n] =  fishes_in_days(6, time) + fishes_in_days(8, time) + 1
  return memoization[days][n]

numbers = open(input_path).readline().split(',')
print(reduce(lambda acc, n: acc + 1 + fishes_in_days(int(n), 80), numbers, 0))
print(reduce(lambda acc, n: acc + 1 + fishes_in_days(int(n), 256), numbers, 0))