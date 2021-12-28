from collections import deque

def bfs(graph, initialNode):
  queue = deque()
  # visited = set()
  queue.append(initialNode)
  # visited.add(initialNode)
  while(queue):
    node = queue.popleft()
    for next_state in graph[node]:
      # if next_state not in visited:
      queue.append(next_state)
    # visited.add(node)
  return graph