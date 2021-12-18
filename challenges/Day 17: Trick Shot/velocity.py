input_path = 'advent_of_code_2021/challenges/Day 17: Trick Shot/input'
from utils import binary_search_velocity_y

x_range, y_range = open(input_path).readline()[len('target area: '):].split(', ')
x_min, x_max = x_range[2:].split('..')
y_min, y_max = y_range[2:].split('..')

step_x = lambda x_pos, x_velocity:  [x_pos + x_velocity, 0 if x_velocity == 0 else x_velocity + (-1 if x_velocity > 0 else 1)]
step_y = lambda y_pos, y_velocity:  [y_pos + y_velocity, y_velocity - 1]

def is_in_diameter_y(y):
  y_pos = 0
  while(True):
    y_pos, y = step_y(y_pos, y)
    if y_pos in range(int(y_min), int(y_max)): return True
    if y_pos < int(y_min) and y < 0: return False

print(binary_search_velocity_y(0, 1000, is_in_diameter_y))  # 5253