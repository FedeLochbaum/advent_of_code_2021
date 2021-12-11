input_path = 'advent_of_code_2021/challenges/Day 11: Dumbo Octopus/input'
from utils import dict_from_file, neighbors
# Part 1
ROWS = 9
COLUMNS = 9
input = dict_from_file(input_path)
steps = 100
total_flashes = 0

def flash(r, c, flashes):
  for _r, _c in neighbors(r, c):
    if (_r < 0 or _c < 0 or _r > ROWS or _c > COLUMNS): continue
    check_flash(_r, _c, flashes); input[_r][_c]+=1

def check_flash(r, c, flashes):
  if(input[r][c] >= 9 and not(r, c) in flashes): flashes.append((r, c)); flash(r, c, flashes)

def simulate_step():
  flashes = []
  for r, _ in enumerate(input):
    for c, _ in enumerate(input[r]):
      check_flash(r, c, flashes); input[r][c]+=1
  
  for (r, c) in flashes: input[r][c] = 0
  return(len(flashes))

for _ in range(steps): total_flashes += simulate_step()
print(total_flashes)