input_path = 'advent_of_code_2021/challenges/Day 24: Arithmetic Logic Unit/input'
from alu import ALU
from reader import Reader

def execute(alu):
  with open(input_path) as f:
    for line in f:
      cmd = line[:-1][:3]
      a = None; b = None
      if (cmd == 'inp'): a = line[:-1][4]
      else: a, b = line[:-1][4:].split(' ')
      getattr(alu, cmd)(a, b)

median = 44444444444444
reader = Reader([])
alu = ALU(reader)

def check_input(number):
  alu.clean()
  input = list(map(int, str(number)))
  if 0 in input: return False
  alu.reader.values = input
  execute(alu)
  if (alu.regs['z'] == 0): print(input); return True
  return False

for i in range(0, 55555555555556):
  if (check_input(median + i) or check_input(median - i)): break