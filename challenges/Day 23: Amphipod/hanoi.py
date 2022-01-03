input_path = 'advent_of_code_2021/challenges/Day 23: Amphipod/input2'
from game import Game, initial_state, room_pos, heuristic, is_goal
from queue import PriorityQueue

UPPER_BOUND = 80000

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

def a_star(graph, initialNode, h):
  pqueue = PriorityQueue()
  visited = set()
  pqueue.put((h(initialNode), initialNode, 0))
  min_cost = UPPER_BOUND
  while not pqueue.empty():
    priority, node, cost = pqueue.get_nowait()
    if is_goal(node):
      min_cost = min(min_cost, cost); continue
    if cost >= min_cost: continue
    for state_cost, next in graph[node]:
      n_cost = cost + state_cost
      if n_cost >= min_cost: continue
      if (str(next), n_cost) not in visited:
        visited.add((str(next), n_cost))
        pqueue.put((
          priority + h(next),
          next,
          n_cost
        ))
  return min_cost

print(a_star(Game(), initial_state(A, B, C, D), heuristic))
# 48541