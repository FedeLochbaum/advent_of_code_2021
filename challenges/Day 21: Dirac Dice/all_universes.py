input_path = 'advent_of_code_2021/challenges/Day 21: Dirac Dice/input'
from game import Game, initial_state, won

with open(input_path) as f: initial = initial_state(f.readline()[-2], f.readline()[-2])

memoization = {}
def play(graph, state):
  if (not state in memoization):
    wins = [0, 0]
    if (len(graph[state]) == 0): wins[0 if won(state, 1) else 1] += 1
    for next_state in graph[state]:
      w0, w1 = play(graph, next_state)
      wins[0] += w0; wins[1] += w1
    memoization[state] = wins
  
  return memoization[state]

print(play(Game(), initial))