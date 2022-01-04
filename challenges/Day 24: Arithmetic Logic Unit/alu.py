# Four-dimensional processing unit
class ALU:
  def __init__(self, reader):
    self.regs = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    self.reader = reader

  def clean(self): self.regs = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
  def value(self, b): return int(b) if not b in self.regs else self.regs[b]
  def inp(self, a, b): self.regs[a] = self.reader.read()
  def add(self, a, b): self.regs[a] += self.value(b)
  def mul(self, a, b): self.regs[a] *= self.value(b)

  def div(self, a, b):
    b = self.value(b)
    if b == 0: return
    self.regs[a] //= b

  def mod(self, a, b):
    b = self.value(b)
    if self.regs[a] < 0 or b <= 0: return
    self.regs[a] %= b

  def eql(self, a, b): self.regs[a] = 1 if self.regs[a] == self.value(b) else 0