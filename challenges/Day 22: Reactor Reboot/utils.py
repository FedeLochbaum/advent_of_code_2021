min_max_sub_str = lambda x: x[2:].split('..')

WIDTH = 50; HEIGHT = 50; DEPTH = 50
interval_limit = [[-WIDTH, -HEIGHT, -DEPTH], [WIDTH, HEIGHT, DEPTH]]

node_by_interval = lambda _int, left, right: { 'int': _int, 'key': _int.low, 'max': max(_int.high, left.max, right.max) } 

point_in_range = lambda point, _range: (
  point[0] in range(_range[0][0], _range[1][0] + 1) and
  point[1] in range(_range[0][1], _range[1][1] + 1) and
  point[2] in range(_range[0][2], _range[1][2] + 1)
)

illegal_interval = lambda interval: (
  interval[0][0] < interval_limit[0][0] or interval[0][1] < interval_limit[0][1] or interval[0][2] < interval_limit[0][2] or 
  interval[1][0] > interval_limit[1][0] or interval[1][1] > interval_limit[1][1] or interval[1][2] > interval_limit[1][2]
)