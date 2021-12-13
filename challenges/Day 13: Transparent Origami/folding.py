input_path = 'advent_of_code_2021/challenges/Day 13: Transparent Origami/input'
import re
ROW = 892; COL = 1310
matrix = ['.' * COL for _ in range(ROW)]

def replace_index(str, index, replacement=''): return '%s%s%s'%(str[:index], replacement, str[index+1:])

def fold_horizontal(n):
  for i in range(n + 1, min(ROW, ((n+1) * 2) - 1)):
    _row = n - (i - n)
    for col, v in enumerate(matrix[i]):
      if v == '#': matrix[_row] = replace_index(matrix[_row], col, '#')
  del matrix[n:ROW]

def fold_vertical(n):
  for col in range(n + 1, min(COL, ((n+1) * 2) - 1)):
    _col = n - (col - n)
    for r, _ in enumerate(matrix):
      if matrix[r][col] == '#': matrix[r] = replace_index(matrix[r], _col, '#')
  for i, _ in enumerate(matrix): matrix[i] = matrix[i][:n]

with open(input_path) as f:
  for line in f:
    if line == '\n': continue
    if (re.match('fold along ', line)):
      dir, n = line[len('fold along '):].split('=')
      (fold_horizontal if dir == 'y' else fold_vertical)(int(n))
    else: col, row = line[:-1].split(','); matrix[int(row)] = replace_index(matrix[int(row)], int(col), '#')

for row in matrix: print(''.join(row))