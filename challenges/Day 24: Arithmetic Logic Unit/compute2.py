input_path = 'advent_of_code_2021/challenges/Day 24: Arithmetic Logic Unit/input'

divs = []; offsets = []; modifiers = []
n_line = 0
with open(input_path) as f:
  for i, line in enumerate(f):
    cmd = line[:-1][:3]
    a = None; b = None
    if (cmd == 'inp'): a = line[:-1][4]
    else: a, b = line[:-1][4:].split(' ')
    n_line = i % 18
    if n_line == 4: divs.append(int(b))
    if n_line == 5: offsets.append(int(b))
    if n_line == 15: modifiers.append(int(b))

def find_number(divs, offsets, modifiers, f):
  z_values = { 0: 0 }
  updated = {}
  for i in range(14):
    for z_key in z_values:
      for n in range(9, 0, -1):
        candidate = z_values[z_key] * 10 + n
        z = int(z_key / divs[i])
        if (((z_key % 26) + offsets[i]) != n): z = z * 26 + n + modifiers[i]
        if (z == 0 and len(str(candidate)) == 14): print(candidate)
        updated[z] = (f(updated[z], candidate) if z in updated else candidate)
    z_values = updated.copy()
  return z_values[0]

# print(find_number(divs, offsets, modifiers, max))
print(find_number(divs, offsets, modifiers, min))