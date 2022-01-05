input_path = 'advent_of_code_2021/challenges/Day 25: Sea Cucumber/input'
from copy import deepcopy
# sea cucumbers = v | >

map = []
steps = 0
with open(input_path) as f:
  for i, line in enumerate(f):
    map.append([])
    for c in line[:-1]: map[i].append(c)

def can_move_right(r, c, map, mutable_map):
  if len(mutable_map[r]) - 1 == c: return map[r][0] == '.'

  return map[r][c + 1] == '.'

def can_move_bottom(r, c, map, mutable_map):
  if len(mutable_map) - 1 == r:
    return (map[0][c] == '.' and not mutable_map[0][c] == '>') or (map[0][c] == '>' and can_move_right(0, c, map, mutable_map))
  elif map[r + 1][c] == '.':
    if c == 0: return map[r+1][len(mutable_map[r+1]) - 1] != '>'
    if map[r+1][c - 1] == '>': return False
    return True
  elif map[r + 1][c] == '>':
    return can_move_right(r+1, c, map, mutable_map)

  return False

def move_bottom(r, c, map, mutable_map):
  # case where mutable_map[r][c] = v
  if can_move_bottom(r, c, map, mutable_map):
    if len(mutable_map) - 1 == r:
      mutable_map[0][c] = 'v'
    else:
      mutable_map[r+1][c] = 'v'
    mutable_map[r][c] = '.'
    return True

  return False

def move_right(r, c, map, mutable_map):
  # case where mutable_map[r][c] = >
  if can_move_right(r, c, map, mutable_map):
    if len(mutable_map[r]) - 1 == c:
      mutable_map[r][0] = '>'
    else:
      mutable_map[r][c+1] = '>'
    mutable_map[r][c] = '.' if mutable_map[r][c] == map[r][c] else mutable_map[r][c]
    return True

  return False

def step(map):
  mutable_map = deepcopy(map)
  movements = 0
  for r, row in enumerate(map):
    for c, elem in enumerate(row):
      if elem == '.': continue
      flag = (move_right if elem == '>' else move_bottom)(r, c, map, mutable_map)
      if flag: movements +=1
  return mutable_map, movements

movements = None
while(movements != 0):
  map, movements = step(map); steps += 1
  # for i in map: print(''.join(i))
  # print('\n')
print(steps)
