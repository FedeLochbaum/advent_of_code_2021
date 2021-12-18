import math

form = lambda n: (n * n/2) + n/2 if n % 2 == 0 else n * (n+1)/2
max_y_pos = lambda y: y if y < 0 else form(y)

def binary_search_velocity_y(_min, _max, is_in_diameter_y):
  while(_min != _max):
    mean = math.floor((_min + _max) / 2)
    if (is_in_diameter_y(mean)): _min = mean
    else: _max = mean
    if (_max == _min + 1):
      return max_y_pos(_max) if is_in_diameter_y(_max) else max_y_pos(_min)
