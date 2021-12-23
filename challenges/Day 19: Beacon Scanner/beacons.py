input_path = 'advent_of_code_2021/challenges/Day 19: Beacon Scanner/test'
import re
import itertools
from collections import deque
from functools import reduce
from scanner import Scanner

combinations = lambda array: reduce(lambda acc, elem: acc + [
  (elem[0], elem[1], elem[2]), (-elem[0], -elem[1], -elem[2]), # all positive, all negative
  (-elem[0], elem[1], elem[2]), (elem[0], -elem[1], elem[2]), (elem[0], elem[1], -elem[2]), # only one negative
  (-elem[0], -elem[1], elem[2]), (-elem[0], elem[1], -elem[2]), (elem[0], -elem[1], -elem[2]) # two negatives
], list(itertools.permutations(array)), [])

get_diff = lambda base_point, _point: (base_point[0] - _point[0], base_point[1] - _point[1], base_point[2] - _point[2])
apply_diff = lambda point, diff: (diff[0] + point[0], diff[1] + point[1], diff[2] + point[2])

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
      current.add_point((int(point[0]), int(point[1]), int(point[2])))

# Warning! this is O(n^4)
def try_connect(base_scanner, scanner_to_connect):
  for point in scanner_to_connect.points:
    all_commbinations = combinations(point)
    for _point in all_commbinations:
      for base_point in base_scanner.points:
        diff = get_diff(base_point, _point)
        with_offset = list(map(lambda p: apply_diff(p, diff), all_commbinations))
        intersection = set(scanner_to_connect.points).intersection(with_offset)
        if len(intersection) >= 12: return diff
  return None

# Solution
while(scanners):
  scanner = scanners.popleft()
  diff = try_connect(scanner_0, scanner)
  if (diff != None):
    print('Descarto scanner: ', scanner.label)
    for point in scanner.points:
      real_point = apply_diff(point, diff)
      if (not real_point in scanner_0.points): scanner_0.add_point(real_point)
  else:
    print('Fallé intentando integrar el scanner: ', scanner.label)
    scanners.append(scanner)

print(len(scanner_0.points))