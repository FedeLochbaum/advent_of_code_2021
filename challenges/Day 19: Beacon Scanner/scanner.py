from functools import reduce
import itertools

def manhattan(a, b): return sum(abs(val2-val1) for val1, val2 in zip(a,b))
  # return sum([abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]) ])
# 

negative_combinations = lambda elem: [
  (elem[0], elem[1], elem[2]), # all positive
  (-elem[0], -elem[1], -elem[2]), # all negative
  (-elem[0], elem[1], elem[2]), (elem[0], -elem[1], elem[2]), (elem[0], elem[1], -elem[2]), # only one negative
  (-elem[0], -elem[1], elem[2]), (-elem[0], elem[1], -elem[2]), (elem[0], -elem[1], -elem[2]) # two negatives
]

get_diff = lambda base_point, _point: (base_point[0] - _point[0], base_point[1] - _point[1], base_point[2] - _point[2])
combinations = lambda array: reduce(lambda acc, elem: acc + negative_combinations(elem), list(itertools.permutations(array)), [])
apply_delta = lambda point, delta: (point[0] * delta[0], point[1] * delta[1], point[2] * delta[2])

def apply_diff_and_delta(point, diff, delta):
  p_with_delta = apply_delta(point, delta)
  return (diff[0] - p_with_delta[0], diff[1] - p_with_delta[1], diff[2] - p_with_delta[2])

def apply_permutation(point, permutation): # (0, 1, 2), (1, 0, 2) ...
  return (point[permutation[0]], point[permutation[1]], point[permutation[2]])

class Scanner:
  def __init__(self, label):
    self.label = label
    self.pos = None
    self.points = []
    self.possibles = {} # 0,0 pos -> all posssibles [(diff, delta, permutation)]
    self.index = {}

  def set_pos(self, pos): self.pos = pos

  def manhattan_distance(self, pos): return manhattan(self.pos, pos)

  def add_point(self, point):
    self.points.append(point)
    self.index[point] = True
  
  def has_point(self, point): return point in self.index

  def get_possibles(self, point):
    if not point in self.possibles:
      self.possibles[point] = []
      for my_point in self.points:
        for _point in combinations(my_point):
          base_diff = get_diff(point, _point)
          if (
            manhattan([base_diff[0]], [point[0]]) > 1000 or
            manhattan([base_diff[1]], [point[1]]) > 1000 or
            manhattan([base_diff[2]], [point[2]]) > 1000
            ) : continue
          for delta in negative_combinations((1, 1, 1)):
            for permutation in itertools.permutations((0, 1, 2)):
              self.possibles[point].append((base_diff, delta, permutation))

    return self.possibles[point]
