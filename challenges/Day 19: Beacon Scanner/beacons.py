input_path = 'advent_of_code_2021/challenges/Day 19: Beacon Scanner/test'
import re
import itertools
from collections import deque
from functools import reduce
from scanner import Scanner

combinations = lambda array: reduce(lambda acc, elem: acc + [
  elem, [-elem[0], -elem[1], -elem[2]],
  [-elem[0], elem[1], elem[2]], [elem[0], -elem[1], elem[2]], [elem[0], elem[1], -elem[2]],
  [-elem[0], -elem[1], elem[2]], [-elem[0], elem[1], -elem[2]],
  [elem[0], -elem[1], -elem[2]]
], list(itertools.permutations(array)), [])

scanners = deque()
scanner_0 = None
current = None
with open(input_path) as f:
  for line in f:
    if line == '\n': continue
    if re.match('--- scanner', line[:-1]):
      label = line[12]
      current = Scanner(label)
      if (label == '0'): scanner_0 = current
      else: scanners.append(current)
    else:
      point = line[:-1].split(',')
      current.add_point([int(point[0]), int(point[1]), int(point[2])])

def try_connect(base_scanner, scanner_to_connect):
  for point in scanner_to_connect.points:
    all_commbinations = combinations(point)
    for _point in all_commbinations: # Warning! this is n^3
      for base_point in base_scanner.points:
        diff = [_point[0] - base_point[0], _point[1] - base_point[1], _point[2] - base_point[2]]
        with_offset = list(map(lambda p: apply_diff(p, diff), all_commbinations))
        if len(list(set(scanner_to_connect.points) & set(with_offset)) >= 12):
          return diff
  return None

def apply_diff(point, diff):
  print('point: ', point)
  return [point[0] - diff[0], point[1] - diff[1], point[2] - diff[2]]

# Solution
while(scanners):
  scanner = scanners.popleft()
  diff = try_connect(scanner_0, scanner)
  if (diff != None):
    for point in scanner.points:
      real_point = apply_diff(point, diff)
      if (not real_point in scanner_0.points): scanner_0.add_point(real_point)
  else:
    scanners.append(scanner)

print(len(scanner_0.points))