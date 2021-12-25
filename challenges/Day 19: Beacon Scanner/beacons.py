input_path = 'advent_of_code_2021/challenges/Day 19: Beacon Scanner/input'
import re
from collections import deque
from scanner import Scanner, apply_diff_and_delta, apply_permutation

LOWER_BOUND = 2

scanners = deque()
scanner_0 = None
current = None
with open(input_path) as f:
  for line in f:
    if line == '\n': continue
    if re.match('--- scanner', line[:-1]):
      label = line[12:14]
      current = Scanner(label)
      if (label == '0 '): scanner_0 = current
      scanners.append(current)
    else:
      point = line[:-1].split(',')
      current.add_point((int(point[0]), int(point[1]), int(point[2])))

def try_match(base_scanner, scanner_to_connect):
  for base_point in base_scanner.points:
    for diff, delta, perm in scanner_to_connect.get_possibles(base_point):
      count = 0
      for p in scanner_to_connect.points:
        count+= 1 if base_scanner.has_point(apply_diff_and_delta(apply_permutation(p, perm), diff, delta)) else 0
      if(count > LOWER_BOUND): return diff, delta, perm
  return None, None, None

# Solution
max_scanners = [scanner_0]
while(scanners):
  scanner = scanners.popleft()
  diff, delta, permutation = try_match(scanner_0, scanner)
  if (diff != None):
    scanner.set_pos(diff)
    del scanner.possibles
    max_scanners.append(scanner)
    for point in scanner.points:
      real_point = apply_diff_and_delta(apply_permutation(point, permutation), diff, delta)
      if (not scanner_0.has_point(real_point)): scanner_0.add_point(real_point)
  else: scanners.append(scanner)

print(len(scanner_0.points))

max_dist = 0
for scanner1 in max_scanners:
  for scanner2 in max_scanners:
    max_dist = max(max_dist, scanner1.manhattan_distance(scanner2.pos))

print(max_dist)