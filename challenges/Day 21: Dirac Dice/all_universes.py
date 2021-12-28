input_path = 'advent_of_code_2021/challenges/Day 21: Dirac Dice/test'
from bfs import bfs
from game import Game, initial_state

with open(input_path) as f: initial = initial_state(f.readline()[-2], f.readline()[-2])

game = bfs(Game(), initial)
print(game.scores)
print(len(game.graph))