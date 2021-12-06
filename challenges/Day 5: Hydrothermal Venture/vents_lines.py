from functools import reduce  
input_path = 'advent_of_code_2021/challenges/Day 5: Hydrothermal Venture/input'

# TODO: avoid to use a matrix
matrix = [ [ 0 for _ in range(1000)] for _ in range(1000)]
collisions = set()

def split_line(line):
  xy1, xy2 = line[:-1].split(' -> ')
  x1, y1 = map(int, xy1.split(','))
  x2, y2 = map(int, xy2.split(','))
  return [min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)]

def check(points):
  for x, y in points:
    key = str(x) + ',' + str(y)
    if (matrix[x][y] > 0): collisions.add(key)
    matrix[x][y] += 1

with open(input_path) as f:
  for line in f:
    x1, y1, x2, y2 = split_line(line)
    if (x1 == x2): check([[x1, y] for y in range(y1, y2 + 1)])
    elif (y1 == y2): check([[x, y1] for x in range(x1, x2 + 1)])
    # else: check([[x, x] for x in range(x1, y2 + 1)])
    # 8,0 -> 0,8

print(len(collisions))

# for row in matrix:
#   print(row)

# 5294
