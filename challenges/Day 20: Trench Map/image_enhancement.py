input_path = 'advent_of_code_2021/challenges/Day 20: Trench Map/input'
from functools import reduce

enhancement = ''
image = []
to_bin = { '.': '0', '#': '1' }

def index_from(r, c, input):
  binary = ''
  for i in range(-1, 2):
    for j in range(-1, 2):
      bin = '0' if (r+i < 0 or r+i > len(input) - 1 or c+j < 0 or c+j > len(input[r+i]) - 1) else to_bin[input[r+i][c+j]]
      binary = binary + bin
  # if(binary == '000000000'): return 3
  return int(binary, 2)

def enhance(input): return [[ enhancement[index_from(r - 2, c - 2, input)] for c in range(len(input[0]) + 4)] for r in range(len(input) + 4)]

enhance_image = lambda input, times: reduce(lambda i, _: enhance(i), range(times), input)

with open(input_path) as f:
  enhancement = f.readline()[:-1]
  for line in f:
    if line == '\n': continue
    image.append(list(line[:-1]))

count = 0
img = enhance_image(image, 2)
for line in img: count += sum(char == '#' for char in line)
for line in img: print(''.join(line))
print(count)