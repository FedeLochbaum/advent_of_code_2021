class Reader:
  def __init__(self, values):
    self.values = values
  
  def read(self): return self.values.pop(0)