input_path = 'advent_of_code_2021/challenges/Day 7: The Treachery of Whales/input'
from functools import reduce
from binary_search import binary_search

numbers = open(input_path).readline().split(',')
def form(num): return (num * num/2) + num/2 if num % 2 == 0 else num * (num+1)/2
def cost_of(value): return reduce(lambda acc, num: acc + form(abs(int(num) - value)), numbers, 0)

min_value, max_value = reduce(
  lambda acc, num: [min(int(num), acc[0]), max(int(num), acc[1])],
  numbers,
  [float('inf'), float('-inf')]
)

print(binary_search(
  min_value,
  max_value,
  cost_of,
  lambda min_cost, max_cost: min_cost < max_cost,
  lambda max_cost, min_cost: max_cost <= min_cost,
))