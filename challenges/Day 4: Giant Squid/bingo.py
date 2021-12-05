from functools import reduce  
input_path = 'advent_of_code_2021/challenges/Day 4: Giant Squid/test'

numbers = []
boards = []
class Board:
  def __init__(self):
    self.rows = []
    self.index = {} # numbers index -> (row, col, marked)

  def add_row(self, row):
    for y, val in enumerate(row):
      self.index[val] = [len(self.rows), y, False]
    self.rows.append(row)

  def won_row(self, x):
    return all(self.index[cell][2] for cell in self.rows[x])

  def won_column(self, y):
    for x in range(5):
      if (not self.index[self.rows[x][y]][2]): return False
    return True

  def annotate(self, val):
    if (self.index[val]):
      x, y, _ = self.index[val]
      self.index[val][2] = True
      return self.won_row(x) or self.won_column(y)
    return False

  def unmarked_sum(self):
    res = 0
    for key in self.index.keys():
      if(not self.index[key][2]):
        res += int(key)
    return res
    # return reduce(lambda n, key: n + int(key) if not self.index[key][2] else 0, self.index.keys(), 0)

# Part 1
with open(input_path) as f:
  # Parsing
  current_board = None
  for i, line in enumerate(f):
    if (i == 0):
      numbers = line[:-1].split(',')
      continue
    
    if(line == '\n'):
      current_board = Board()
      boards.append(current_board)
      continue
    
    if (current_board):
      current_board.add_row(line.split())

  # Solving
  cut = False
  for num in numbers:
    print('num: ', num)
    for board in boards:
      if (board.annotate(num)):
        print(board.unmarked_sum() * int(num))
        cut = True
        break
    if (cut): break
