import math

def binary_search(_min, _max, func, check_min, check_max):
  while(_min != _max):
    _min_cost = func(_min)
    _max_cost = func(_max)
    mean = math.floor((_min + _max) / 2)
    if (check_min(_min_cost,_max_cost)): res = _min_cost; _max = mean
    if (check_max(_max_cost, _min_cost)): res = _max_cost; _min = mean
    if (_max == _min + 1): res = func(mean); break
  return res
