input_path = 'advent_of_code_2021/challenges/Day 22: Reactor Reboot/input'
from utils import min_max_sub_str, illegal_interval, point_in_range

cubes = set()
count = 0
with open(input_path) as f:
  for line in f:
    on = line[0:2] == 'on'
    x, y, z = line[(3 if on else 4):-1].split(',')
    x_min, x_max = min_max_sub_str(x)
    y_min, y_max = min_max_sub_str(y)
    z_min, z_max = min_max_sub_str(z)
    interval = [[int(x_min), int(y_min), int(z_min)], [int(x_max), int(y_max), int(z_max)]]
    if (not illegal_interval(interval)):
      if on:
        for _x in range(interval[0][0], interval[1][0] + 1):
          for _y in range(interval[0][1], interval[1][1] + 1):
            for _z in range(interval[0][2], interval[1][2] + 1):
              point = (_x, _y, _z)
              if not point in cubes: 
                count += 1
                cubes.add(point)
      else:
        for point in cubes.copy():
          if(point_in_range(point, interval)):
            count -= 1
            cubes.remove(point)

print(count)