input_path = 'advent_of_code_2021/challenges/Day 15: Chiton/input'
from utils import shortest_path, dict_from_file, point_by

ROW = 100
COL = 100

print(shortest_path(dict_from_file(input_path), ROW, COL, point_by(0, 0), point_by(99, 99)))