
input_path = 'advent_of_code_2021/challenges/Day 1: Sonar Sweep/input.txt'
# Part 1
times = -1
last = float('-inf')
with open(input_path) as f:
  for line in f:
    current = float(line)
    if (current > last):
      times+=1
    last = current

print(times)

# Part 2
times = 0
i = 0
window = { 0: 0, 1: 0, 2: 0, 'sum': 0 }

# TODO: use only a string and shift it
def add(num):
  window['sum'] = (window['sum'] - window[2]) + num
  window[2] = window[1]
  window[1] = window[0]
  window[0] = num

with open(input_path) as f:
  for line in f:
    i+=1
    sum = window['sum']
    add(float(line))
    if ( i > 3 and window['sum'] > sum ):
      times+=1

print(times)