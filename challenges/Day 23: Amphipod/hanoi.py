input_path = 'advent_of_code_2021/challenges/Day 23: Amphipod/test'
from game import Game, initial_state, room_pos, is_goal
from collections import deque

A = []; B = []; C = []; D = []
memoization = {}
with open(input_path) as f:
  for row, line in enumerate(f):
    for col, c in enumerate(line[:-1]):
      if row in range(2, 4):
        if col == room_pos['A'] + 1: A.append(c)
        elif col == room_pos['B'] + 1: B.append(c)
        elif col == room_pos['C'] + 1: C.append(c)
        elif col == room_pos['D'] + 1: D.append(c)

def play_bfs(graph, initial_node, is_goal):
  queue = deque()
  visited = set()
  queue.append((initial_node, 0))
  visited.add(str(initial_node))
  costs = []
  while(queue):
    node, cost = queue.popleft()
    if is_goal(node): costs.append(cost); continue
    for state_cost, next in graph[node]:
      if str(next) not in visited:
        visited.add(str(next))
        queue.append((next, cost + state_cost))
  return costs

print(min(play_bfs(Game(), initial_state(A, B, C, D), is_goal)))