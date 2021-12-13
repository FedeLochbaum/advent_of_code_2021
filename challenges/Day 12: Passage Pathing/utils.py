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

def copy_without(visited, elem):
  copy = visited.copy()
  copy.remove(elem)
  return copy

def find_paths(graph, _from, _to, visited, selected):
  paths = []
  if _from == _to: return [_to]
  if (_from.islower()): visited.add(_from)

  # TODO: Move to use a queue
  for neighbor in graph[_from]:
    if (neighbor not in visited):
      paths = find_paths(graph, neighbor, _to, visited.copy(), selected) + paths

    # paths = find_paths(graph, neighbor, _to, copy_without(visited, _from), True) if (other_selected == False and _from.islower() and _from != 'start') else paths
  return paths
