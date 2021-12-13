input_path = 'advent_of_code_2021/challenges/Day 13: Transparent Origami/input'
import re
ROW = 892; COL = 1310
sum = 0
matrix = [['.' for _ in range(COL)] for _ in range(ROW)]
def fold_horizontal(n):
  for i in range(n + 1, ROW):
    for col, v in enumerate(matrix[i]):
      matrix[n - (i - n)][col] = v if (v == '#') else matrix[n - (i - n)][col]
  del matrix[n:ROW]

def fold_vertical(n):
  for r, _ in enumerate(matrix):
    for col in range(n + 1, COL):
      _col = n - (col - n)
      matrix[r][_col] = '#' if (matrix[r][col] == '#') else matrix[r][_col]
    del matrix[r][n:COL]

with open(input_path) as f:
  for line in f:
    if line == '\n': complete = True; continue
    if (re.match('fold along ', line)):
      dir, n = line[len('fold along '):].split('=')
      (fold_horizontal if dir == 'y' else fold_vertical)(int(n)); break
    else: col, row = line[:-1].split(','); matrix[int(row)][int(col)] = '#'

for row in matrix: sum +=''.join(row).count('#')
print(sum)
# for row in matrix: print(row)