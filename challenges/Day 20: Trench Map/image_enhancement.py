input_path = 'advent_of_code_2021/challenges/Day 20: Trench Map/input'
from functools import reduce

enhancement = ''; image = []; to_bin = { '.': '0', '#': '1' }

enhance = lambda input, it: [[ enhanced_value(r - 2, c - 2, input, it) for c in range(len(input[0]) + 4)] for r in range(len(input) + 4)]
enhance_image = lambda input, times: reduce(lambda img, it: enhance(img, it), range(times), input)

def enhanced_value(r, c, input, it):
  default = '0' if it % 2 == 0 else '1'
  in_range = lambda p: p[0] in range(0, len(input)) and p[1] in range(0, len(input[0]))
  points = [ [r + r_delta, c + c_delta] for r_delta in range(-1, 2) for c_delta in range(-1, 2)]
  binary = ''.join(map(lambda p: to_bin[input[p[0]][p[1]]] if in_range(p) else default, points))
  return enhancement[int(binary, 2)]

with open(input_path) as f:
  enhancement = f.readline()[:-1]
  for line in f:
    if line == '\n': continue
    image.append(list(line[:-1]))

count = 0
for line in enhance_image(image, 50): count += sum(char == '#' for char in line)
print(count)