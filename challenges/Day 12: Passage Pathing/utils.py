def graph_from_file(input_path):
  graph = {}
  with open(input_path) as f:
    for line in f:
      _from, _to = line[:-1].split('-')
      if (not _from in graph): graph[_from] = []
      if (not _to in graph): graph[_to] = []
      graph[_from].append(_to)
      graph[_to].append(_from)
  return graph

def find_paths(graph, _from, _to, visited_small_keys):
  paths = []
  if (_from.islower()): visited_small_keys.add(_from)
  if _from == _to: return [_to]

  # TODO: Move to use a queue
  for neighbor in graph[_from]:
    if neighbor not in visited_small_keys:
      paths = paths + find_paths(graph, neighbor, _to, visited_small_keys.copy())
  return paths
