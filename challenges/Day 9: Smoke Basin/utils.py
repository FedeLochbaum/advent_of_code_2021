def dict_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([num for num in line[:-1]])
  return array
