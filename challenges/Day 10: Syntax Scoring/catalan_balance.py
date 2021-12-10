input_path = 'advent_of_code_2021/challenges/Day 10: Syntax Scoring/input'
from collections import deque
from functools import reduce
open_delimiters = ['(', '[', '{', '<']
delimiters = { '(': ')', '[': ']', '{': '}', '<': '>' }
points_by_end_delimiter = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
points_by_delimiter = { '(': 1, '[': 2, '{': 3, '<': 4 }

stack_score = lambda stack: reduce(lambda score, delimiter: (score * 5) + points_by_delimiter[delimiter], list(stack)[::-1], 0)

corrupted_score = 0
incomplete_scores = []
with open(input_path) as f:
  for line in f:
    stack = deque(); ignore = False
    for delimiter in line[:-1]:
      if (delimiter in open_delimiters): stack.append(delimiter); continue
      if (delimiter == delimiters[stack[-1]]): stack.pop(); continue
      corrupted_score += points_by_end_delimiter[delimiter]; ignore = True; break
    if (len(stack) != 0 and not ignore): incomplete_scores.append(stack_score(stack))
print('corrupted_score: ', corrupted_score, 'incomplete score winner: ', sorted(incomplete_scores)[int((len(incomplete_scores) - 1) / 2)])