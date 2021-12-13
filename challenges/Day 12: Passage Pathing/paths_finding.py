input_path = 'advent_of_code_2021/challenges/Day 12: Passage Pathing/test_01'
from utils import graph_from_file, find_paths

graph = graph_from_file(input_path)
print(len(find_paths(graph, 'start', 'end', set(), None)))
# 4186