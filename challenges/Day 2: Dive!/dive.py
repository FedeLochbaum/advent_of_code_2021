input_path = 'advent_of_code_2021/challenges/Day 2: Dive!/input'

x, y = 0, 0
commands = {
  'forward': lambda n: [x+n, y],
  'up': lambda n: [x, y-n],
  'down': lambda n: [x, y+n],
}

# Part 1
with open(input_path) as f:
  for line in f:
    command, n = line.split()
    x, y = commands[command](int(n))

print(x * y)

# Part 2
x, y, aim = 0, 0, 0
commands = {
  'forward': lambda n: [x+n, y+(aim*n) , aim],
  'up': lambda n: [x, y, aim-n],
  'down': lambda n: [x, y, aim+n],
}

with open(input_path) as f:
  for line in f:
    command, n = line.split()
    x, y, aim = commands[command](int(n))

print(x * y)