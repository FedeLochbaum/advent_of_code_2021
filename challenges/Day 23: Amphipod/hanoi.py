input_path = 'advent_of_code_2021/challenges/Day 23: Amphipod/test2'
from game import Game, initial_state, room_pos, is_goal
from collections import deque

A = []; B = []; C = []; D = []
memoization = {}
with open(input_path) as f:
  for row, line in enumerate(f):
    for col, c in enumerate(line[:-1]):
      if row in range(2, 6):
        if col == room_pos['A'] + 1: A.append(c)
        elif col == room_pos['B'] + 1: B.append(c)
        elif col == room_pos['C'] + 1: C.append(c)
        elif col == room_pos['D'] + 1: D.append(c)

def play_bfs(graph, initial_node, is_goal):
  queue = deque()
  visited = set()
  queue.append((initial_node, 0))
  visited.add((str(initial_node), 0))
  min_cost = float('inf')
  while(queue):
    node, cost = queue.popleft()
    if is_goal(node):
      print('a comparar: ', cost, min_cost)
      min_cost = min(min_cost, cost); continue
    if cost >= min_cost: continue
    for state_cost, next in graph[node]:
      n_cost = cost + state_cost
      if n_cost >= min_cost: continue
      if (str(next), n_cost) not in visited:
        visited.add((str(next), n_cost))
        queue.append((next, n_cost))
  return min_cost

def play_dfs(graph, initial_node, is_goal):
  stack = deque()
  visited = set()
  stack.append((initial_node, 0))
  visited.add((str(initial_node), 0))
  min_cost = float('inf')
  while(stack):
    node, cost = stack.pop()
    if is_goal(node):
      print('a comparar: ', cost, min_cost)
      min_cost = min(min_cost, cost); continue
    if cost >= min_cost: continue
    for state_cost, next in graph[node]:
      n_cost = cost + state_cost
      if n_cost >= min_cost: continue
      if (str(next), n_cost) not in visited:
        visited.add((str(next), n_cost))
        stack.append((next, n_cost))
  return min_cost

# print(play_bfs(Game(), initial_state(A, B, C, D), is_goal))
print(play_dfs(Game(), initial_state(A, B, C, D), is_goal))