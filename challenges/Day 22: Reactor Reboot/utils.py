min_max_sub_str = lambda x: x[2:].split('..')

class Point:
  def __init__(self, _int):
    self.graph = {}
    self.int = _int
class Interval:
  def __init__(self, _min, _max):
    self.min = _min
    self.max = _max

  def count(self): return (
    abs(self.max.int[0] - self.min.int[0] + 1) *
    abs(self.max.int[1] - self.min.int[1] + 1) *
    abs(self.max.int[2] - self.min.int[2] + 1)
  )

  def intersect(self, interval):
    min_point = Point([max(self.min.int[0], interval.min.int[0]), max(self.min.int[1], interval.min.int[1]), max(self.min.int[2], interval.min.int[2])])
    max_point = Point([min(self.max.int[0], interval.max.int[0]), min(self.max.int[1], interval.max.int[1]), min(self.max.int[2], interval.max.int[2])])
    if (min_point.int[0] > max_point.int[0] or min_point.int[1] > max_point.int[1] or min_point.int[2] > max_point.int[2]): return None
    return Interval(min_point, max_point)

point_in_range = lambda point, _range: (
  point[0] in range(_range[0][0], _range[1][0] + 1) and
  point[1] in range(_range[0][1], _range[1][1] + 1) and
  point[2] in range(_range[0][2], _range[1][2] + 1)
)
