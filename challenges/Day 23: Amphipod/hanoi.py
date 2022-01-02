input_path = 'advent_of_code_2021/challenges/Day 23: Amphipod/test'
from game import Game, initial_state, room_pos, is_goal

A = []; B = []; C = []; D = []
memoization = {}
with open(input_path) as f:
  for row, line in enumerate(f):
    for col, c in enumerate(line[:-1]):
      if row in range(2, 4):
        if col == room_pos['A']: A.append(c)
        elif col == room_pos['B']: B.append(c)
        elif col == room_pos['C']: C.append(c)
        elif col == room_pos['D']: D.append(c)


from collections import deque

def play_bfs(graph, initial_node, is_goal):
  queue = deque()
  visited = set()
  queue.append((initial_node, 0))
  visited.add(str(initial_node))
  while(queue):
    node, cost = queue.popleft()
    print('node, cost ', node, cost )
    if is_goal(node):
      print('solution: ', node, cost)
      continue
      # return node, cost
    for state_cost, next in graph[node]:
      if str(next) not in visited:
        visited.add(str(next))
        queue.append((next, cost + state_cost))
  return None

print(play_bfs(Game(), initial_state(A, B, C, D), is_goal))