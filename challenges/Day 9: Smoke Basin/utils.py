from collections import deque
window_points = lambda r, c: [[r, c-1], [r-1, c], [r, c+1], [r+1, c]]
def dict_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([num for num in line[:-1]])
  return array

def bfs(graph, initialNode):
  queue = deque()
  visited = set()
  queue.append(initialNode)
  visited.add((initialNode[0], initialNode[1]))
  while(queue):
    row, col = queue.popleft()
    for _r, _c in window_points(row, col):
      if (_r < 0 or _c < 0 or _r > 99 or _c > 99 or (graph[_r][_c] == '9')): continue
      if (_r, _c) not in visited: visited.add((_r, _c)); queue.append([_r, _c])
  return visited

connected_component = bfs