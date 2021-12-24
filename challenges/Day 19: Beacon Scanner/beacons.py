input_path = 'advent_of_code_2021/challenges/Day 19: Beacon Scanner/test'
import re
import itertools
from collections import deque
from functools import reduce
from scanner import Scanner

negative_combinations = lambda elem: [
  (elem[0], elem[1], elem[2]), # all positive
  (-elem[0], -elem[1], -elem[2]), # all negative
  (-elem[0], elem[1], elem[2]), (elem[0], -elem[1], elem[2]), (elem[0], elem[1], -elem[2]), # only one negative
  (-elem[0], -elem[1], elem[2]), (-elem[0], elem[1], -elem[2]), (elem[0], -elem[1], -elem[2]) # two negatives
]

combinations = lambda array: reduce(lambda acc, elem: acc + negative_combinations(elem), list(itertools.permutations(array)), [])
get_diff = lambda base_point, _point: (base_point[0] - _point[0], base_point[1] - _point[1], base_point[2] - _point[2])
apply_delta = lambda point, delta: (point[0] * delta[0], point[1] * delta[1], point[2] * delta[2])

def apply_diff_and_delta(point, diff, delta):
  p_with_delta = apply_delta(point, delta)
  return (diff[0] - p_with_delta[0], diff[1] - p_with_delta[1], diff[2] - p_with_delta[2])

def apply_permutation(point, permutation): # (0, 1, 2), (1, 0, 2) ...
  return (point[permutation[0]], point[permutation[1]], point[permutation[2]])

LOWER_BOUND = 11

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

def check_diff(base_scanner, scanner, diff):
  for delta in negative_combinations((1, 1, 1)):
    for permutation in list(itertools.permutations((0, 1, 2))):
      count = 0
      for p in scanner.points:
        with_delta = apply_diff_and_delta(apply_permutation(p, permutation), diff, delta)

        if with_delta in base_scanner.points: count+=1
      if(count > LOWER_BOUND): return diff, delta, permutation
  return None, None, None

def try_connect(base_scanner, scanner_to_connect):
  for point in scanner_to_connect.points:
    all_combinations = combinations(point)
    for _point in all_combinations:
      for base_point in base_scanner.points:
        diff, delta, permutation = check_diff(base_scanner, scanner, get_diff(base_point, _point))
        if diff != None: return diff, delta, permutation
  return None, None, None

# Solution
while(scanners):
  scanner = scanners.popleft()
  diff, delta, permutation = try_connect(scanner_0, scanner)
  if (diff != None):
    print('diff que matchea:', diff, ' con scanner: ', scanner.label)
    for point in scanner.points:
      real_point = apply_diff_and_delta(apply_permutation(point, permutation), diff, delta)
      if (not real_point in scanner_0.points): scanner_0.add_point(real_point)
  else:
    scanners.append(scanner)

print(len(scanner_0.points))