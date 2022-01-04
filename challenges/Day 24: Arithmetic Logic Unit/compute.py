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

alu = ALU(None)
for i in range(11111111111111, 99999999999999):
  input = list(map(int, str(i)))
  alu.reader = Reader(input)
  execute(alu)
  if (alu.regs['z'] == 0): print(input); break