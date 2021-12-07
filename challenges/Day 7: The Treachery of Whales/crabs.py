input_path = 'advent_of_code_2021/challenges/Day 7: The Treachery of Whales/input'
from functools import reduce
import math

a = float('inf')  #0
b = float('-inf') #1859
min_fuel = float('inf')

numbers = open(input_path).readline().split(',')
for n in numbers: b = max(int(n), b); a = min(int(n), a)
while(a != b):
  a_cost = reduce(lambda acc, n: acc + abs(int(n) - a), numbers, 0)
  b_cost = reduce(lambda acc, n: acc + abs(int(n) - b), numbers, 0)
  m = math.floor((a + b) / 2)
  if (a_cost < b_cost): min_fuel = a_cost; b = m
  if (b_cost <= a_cost): min_fuel = b_cost; a = m
print(min_fuel, ' point: ', a)
# 352707