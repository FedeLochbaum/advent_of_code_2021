input_path = 'advent_of_code_2021/challenges/Day 17: Trick Shot/input'
from utils import binary_search_velocity_y

x_range, y_range = open(input_path).readline()[len('target area: '):].split(', ')
x_min, x_max = x_range[2:].split('..')
y_min, y_max = y_range[2:].split('..')

all = set()
step_x = lambda x_pos, x_velocity:  [x_pos + x_velocity, 0 if x_velocity == 0 else x_velocity + (-1 if x_velocity > 0 else 1)]
step_y = lambda y_pos, y_velocity:  [y_pos + y_velocity, y_velocity - 1]

x_pos_in_diameter = lambda x_pos: x_pos in range(int(x_min), int(x_max) + 1)
y_pos_in_diameter = lambda y_pos: y_pos in range(int(y_min), int(y_max) + 1)

point_is_in_diameter = lambda x_pos, y_pos: x_pos_in_diameter(x_pos) and y_pos_in_diameter(y_pos)

def is_in_diameter(z, step, _min, _max, false_cond):
  pos = 0
  while(True):
    pos, z = step(pos, z)
    if pos in range(int(_min), int(_max)): return True
    if false_cond(z, pos): return False

def velocity_in_in_range(x, y):
  x_pos = 0; y_pos = 0
  while(True):
    x_pos, x = step_x(x_pos, x)
    y_pos, y = step_y(y_pos, y)
    if (point_is_in_diameter(x_pos, y_pos)): return True
    if x_pos > int(x_max) or (x == 0 and not x_pos_in_diameter(x_pos)): return False
    if y_pos < int(y_min) and y < 0: return False

is_in_diameter_y = lambda y: is_in_diameter(y, step_y, y_min, y_max, lambda y, pos: pos < int(y_min) and y < 0)

# Part 1
print(binary_search_velocity_y(0, 500, is_in_diameter_y))
# Part 2
# TODO: use binary search to find the optimal min, max for each axis
for x in range(0,  int(x_max) + 1):
  for y in range(int(y_min), max(int(x_max), int(y_max)) + 1):
    if(velocity_in_in_range(x, y)): all.add((x, y))
print(len(all))