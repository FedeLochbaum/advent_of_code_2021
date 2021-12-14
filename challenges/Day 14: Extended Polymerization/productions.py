input_path = 'advent_of_code_2021/challenges/Day 14: Extended Polymerization/input'
productions = {}
count = {}
string = ''
steps = 10
def add_at_index(str, index, replacement=''): return '%s%s%s'%(str[:index], replacement, str[index:])

def prod(string):
  i = 0; j = 1 # iterators
  while (j <= len(string)):
    current = string[i:j+1]
    if(current in productions):
      char = productions[current]
      count[char] = count[char] + 1 if char in count else 1
      string = add_at_index(string, j, char)
      i+=1; j+=1
    i+=1; j+=1
  return string

with open(input_path) as f:
  for i, line in enumerate(f):
    if i == 0:
      for char in line[:-1]: count[char] = count[char] + 1 if char in count else 1
      string = line[:-1]
    if (i > 1):
      pattern, production = line[:-1].split(' -> ')
      productions[pattern] = production

for _ in range(steps): string = prod(string)

print(count)
# print('string:', string)
# print('productions:', productions)
