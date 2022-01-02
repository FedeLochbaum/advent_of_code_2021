input_path = 'advent_of_code_2021/challenges/Day 23: Amphipod/test'
from game import Game, initial_state, room_pos

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

def play(graph, state, current):
  str_state = str(state)
  if (not str_state in memoization):
    memoization[str_state] = current + (0 if len(graph[state]) == 0 else min(map(lambda next: play(graph, next[1], next[0]), graph[state])))
  return memoization[str_state]

print(play(Game(), initial_state(A, B, C, D), 0))