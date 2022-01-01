input_path = 'advent_of_code_2021/challenges/Day 22: Reactor Reboot/test'
from intervaltree import IntervalTree
WIDTH = 50; HEIGHT = 50; DEPTH = 50
interval_limit = [[-WIDTH, -HEIGHT, -DEPTH], [WIDTH, HEIGHT, DEPTH]]

def threeDtoOneD(_int): return _int[0] + (_int[1] * HEIGHT) + (_int[2] * DEPTH * HEIGHT)

def oneDtoThreeD(_x):
  z = _x // (DEPTH * HEIGHT)
  _x -= z * DEPTH * HEIGHT
  y = _x // HEIGHT
  x = _x % WIDTH
  return [x, y, z]

class Interval:
  def __init__(self, _min, _max):
    self.min = _min
    self.max = _max

class Point:
  def __init__(self, _int):
    self.graph = {}
    self.int = _int
    self.oneD = None

  def toOneD(self):
    self.oneD = self.oneD or threeDtoOneD(self.shifted())
    return self.oneD

  def toThreeD(self): return self.unshifted(oneDtoThreeD(self.toOneD()))

  def shifted(self): return [self.int[0] + WIDTH, self.int[1] + HEIGHT, self.int[2] + DEPTH]
  def unshifted(self, _int): return [_int[0] - WIDTH, _int[1] - HEIGHT, _int[2] - DEPTH]

min_max_sub_str = lambda x: x[2:].split('..')

node_by_interval = lambda _int, left, right: { 'int': _int, 'key': _int.low, 'max': max(_int.high, left.max, right.max) } 

in_range_limit = lambda inverval: (
  inverval[0][0] >= interval_limit[0][0] and inverval[1][0] <= interval_limit[1][0] and
  inverval[0][1] >= interval_limit[0][1] and inverval[1][1] <= interval_limit[1][1] and
  inverval[0][2] >= interval_limit[0][2] and inverval[1][2] <= interval_limit[1][2]
)

tree = IntervalTree()
with open(input_path) as f:
  for line in f:
    on = line[0:2] == 'on'
    x, y, z = line[(3 if on else 4):-1].split(',')
    x_min, x_max = min_max_sub_str(x)
    y_min, y_max = min_max_sub_str(y)
    z_min, z_max = min_max_sub_str(z)
    interval = [[int(x_min), int(y_min), int(z_min)], [int(x_max), int(y_max), int(z_max)]]
    if (in_range_limit(interval)):
      min = [int(x_min), int(y_min), int(z_min)]
      max = [int(x_max), int(y_max), int(z_max)]
      interval = Interval(Point(min), Point(max))
      # if on: tree.addi(interval.min.toOneD(), interval.max.toOneD(), interval)
      # else: tree.remove_overlap(interval.min.toOneD(), interval.max.toOneD())

for i in tree.items():
  print(i)
  # _min = i.data.min.int
  # _max = i.data.max.int
  # print(_min.toThreeD())
  # print(_max.toThreeD())
  # print( abs(_max[0] - _min[0]) * abs(_max[1] - _min[1]) * abs(_max[2] - _min[2]))