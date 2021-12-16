input_path = 'advent_of_code_2021/challenges/Day 15: Chiton/input'
from utils import shortest_path, dict_from_file, point_by

ROW = 100
COL = 100

# print(shortest_path(dict_from_file(input_path), ROW, COL, point_by(0, 0), point_by(99, 99)))
graph0 = dict_from_file(input_path)
graph = [[ 0 for _ in range(COL * 5)] for _ in range(ROW * 5)]
for row in range(ROW * 5):
  for col in range(COL * 5):
    original_i = row % ROW
    original_c = col % COL
    n = (row // ROW) + (col // COL) - 1
    graph[row][col] = (graph0[original_i][original_c] + n) % 9 + 1

print(shortest_path(graph, ROW * 5, COL * 5, point_by(0, 0), point_by(499, 499)))