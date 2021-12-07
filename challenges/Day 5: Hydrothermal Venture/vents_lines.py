from functools import reduce
input_path = 'advent_of_code_2021/challenges/Day 5: Hydrothermal Venture/input'

# TODO: avoid to use a matrix
matrix = [[ 0 for _ in range(1000)] for _ in range(1000)]
collisions = set()

def split_line(line):
  xy1, xy2 = line[:-1].split(' -> ')
  x1, y1 = map(int, xy1.split(','))
  x2, y2 = map(int, xy2.split(','))
  return [x1, y1, x2, y2, min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)]

def check(points):
  for x, y in points:
    if matrix[x][y] > 0: collisions.add(str(x) + ',' + str(y))
    matrix[x][y] += 1

with open(input_path) as f:
  for line in f:
    x1, y1, x2, y2, minX, minY, maxX, maxY = split_line(line)
    if x1 == x2: check([[x1, y] for y in range(minY, maxY + 1)])
    elif y1 == y2: check([[x, y1] for x in range(minX, maxX + 1)])
    else: 
      _x1, _y1, _x2, _ = [x1, y1, x2, y2] if minY == y1 else [x2, y2, x1, y2]
      check([[_x1 - i, _y1 + i] if _x1 > _x2 else [_x1 + i, _y1 + i] for i in range(abs(_x2 - _x1) + 1)])

print(len(collisions))