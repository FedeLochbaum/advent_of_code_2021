input_path = 'advent_of_code_2021/challenges/Day 20: Trench Map/test'
from functools import reduce

enhancement = ''
image = []
to_bin = { '.': '0', '#': '1' }

def index_from(r, c, input):
  binary = ''
  for i in range(-1, 2):
    for j in range(-1, 2):
      bin = ('0' if r+i < 0 or r+i > (len(input) - 1) or c+j < 0 or c+j > (len(input[r+i]) - 1) else to_bin[input[r+i][c+j]])
      binary = binary + bin
  return int(binary, 2)

def enhance(input):
  enhanced = []
  cols = len(input[0])
  for r in range(len(input) + 2):
    enhanced.append('')
    for c in range(cols + 2):
      enhanced[r] = enhanced[r] + enhancement[index_from(r-1, c-1, input)]
  return enhanced

enhance_image = lambda input, times: reduce(lambda i, _: enhance(i), range(times), input)

with open(input_path) as f:
  enhancement = f.readline()[:-1]
  for line in f:
    if line == '\n': continue
    image.append(line[:-1])

count = 0
for line in enhance_image(image, 2): count += sum(char == '#' for char in line)
print(count)