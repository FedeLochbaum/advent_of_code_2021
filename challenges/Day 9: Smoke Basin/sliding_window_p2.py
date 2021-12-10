input_path = 'advent_of_code_2021/challenges/Day 9: Smoke Basin/input'
from utils import dict_from_file, window_points, connected_component
import math
input = dict_from_file(input_path)
ROWS, COLUMNS = 99, 99
basins = []

def is_minimal(r, c, num):
  for _r, _c in window_points(r, c):
    if (_r < 0 or _c < 0 or _r > ROWS or _c > COLUMNS): continue
    if (num >= input[_r][_c]): return False
  return True

for r, row in enumerate(input):
  for c, num in enumerate(input[r]):
    if(is_minimal(r, c, num)): basins.append(len(connected_component(input, [r, c])))
print(math.prod(sorted(basins, reverse=True)[:3]))