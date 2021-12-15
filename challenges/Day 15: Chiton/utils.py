from queue import PriorityQueue
neighbors = lambda r, c: [[r, c-1], [r-1, c], [r, c+1], [r+1, c]]

point_by = lambda row, col: f'{row}' + ',' + f'{col}'

def dict_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([int(num) for num in line[:-1]])
  return array

def distance_obj(row, col):
  distance = {}
  for i in range(row):
    for j in range(col):
      distance[point_by(i, j)] = float('inf')
  return distance

def processed_obj(row, col):
  processed = {}
  for i in range(row):
    for j in range(col):
      processed[point_by(i, j)] = False
  return processed

def dijkstra(graph, row, col, initial, final):
  queue = PriorityQueue()
  processed = processed_obj(row, col)
  distance = distance_obj(row, col)
  distance[initial] = 0
  queue.put((0, initial))
  while not queue.empty():
    _, point = queue.get()
    if(processed[point]): continue
    processed[point] = True
    a, b = point.split(',')
    for _r, _c in neighbors(int(a), int(b)):
      neighbor = point_by(_r, _c)
      if (_r < 0 or _c < 0 or _r >= row or _c >= col): continue
      if (distance[point] + graph[_r][_c] < distance[neighbor]):
        distance[neighbor] = distance[point] + graph[_r][_c]
        queue.put((distance[neighbor], neighbor))
  return distance[final]

shortest_path = dijkstra