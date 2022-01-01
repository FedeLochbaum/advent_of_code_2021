input_path = 'advent_of_code_2021/challenges/Day 22: Reactor Reboot/test0'
from utils import min_max_sub_str, Interval, Point
from functools import reduce

commands = []
with open(input_path) as f:
  for line in f:
    on = line[0:2] == 'on'
    x, y, z = line[(3 if on else 4):-1].split(',')
    x_min, x_max = min_max_sub_str(x)
    y_min, y_max = min_max_sub_str(y)
    z_min, z_max = min_max_sub_str(z)
    min = [int(x_min), int(y_min), int(z_min)]
    max = [int(x_max), int(y_max), int(z_max)]
    commands.append((on, Interval(Point(min), Point(max))))

merge = []
cuboids = []
for cmd in commands:
  on, interval = cmd
  if on: merge.append((cmd, interval))
  for c in cuboids:
    intersect = c[1].intersect(interval)
    if intersect: merge.append((False, intersect))
  cuboids = cuboids + merge.copy()
  # std::ranges::copy(merge, std::back_insert_iterator(cuboids))

print(reduce(lambda acc, cmd: acc + ((1 if cmd[0] else -1) * cmd[1].count()), cuboids, 0))