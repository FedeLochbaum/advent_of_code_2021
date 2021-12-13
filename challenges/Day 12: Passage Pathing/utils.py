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

def find_paths(graph, _from, _to, visited, other_selected = False):
  paths = []
  if (_from.islower()): visited.add(_from)
  if _from == _to: return [_to]

  # TODO: Move to use a queue
  for neighbor in graph[_from]:
    paths = find_paths(graph, neighbor, _to, visited.copy()) + paths if neighbor not in visited else paths
  return paths
