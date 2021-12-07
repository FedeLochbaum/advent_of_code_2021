input_path = 'advent_of_code_2021/challenges/Day 7: The Treachery of Whales/input'
from functools import reduce
import math

a = float('inf')
b = float('-inf')
min_fuel = float('inf')

numbers = open(input_path).readline().split(',')
for n in numbers: b = max(int(n), b); a = min(int(n), a)
def form(n): return (n * n/2) + n/2 if n % 2 == 0 else n * (n+1)/2
def cost_of(m): return reduce(lambda acc, n: acc + form(abs(int(n) - m)), numbers, 0)
while(a != b):
  a_cost = cost_of(a)
  b_cost = cost_of(b)
  m = math.floor((a + b) / 2)
  if (a_cost < b_cost): min_fuel = a_cost; b = m
  if (b_cost <= a_cost): min_fuel = b_cost; a = m
  if(b == a + 1): min_fuel = cost_of(m); break
print(min_fuel)