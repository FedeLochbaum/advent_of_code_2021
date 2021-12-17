
import math
simple_hex_to_bin = { '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
  '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010',
  'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

op_by_id_obj = { 0: 'ADD', 1: 'TIMES', 2: 'MIN', 3: 'MAX', 5: 'GT', 6: 'LT', 7: 'EQ' }

apply_to_children = lambda f: lambda ast: f(map(eval, ast['children']))
apply_comp = lambda f: lambda ast: 1 if f(eval(ast['children'][0]), eval(ast['children'][1])) else 0
get_value = lambda ast: ast['value']

eval_function_by_type = {
  'ADD': apply_to_children(sum),
  'TIMES': apply_to_children(math.prod),
  'MIN': apply_to_children(min),
  'MAX': apply_to_children(max),
  'NUM': get_value,
  'GT': apply_comp(lambda x, y: x > y),
  'LT': apply_comp(lambda x, y: x < y),
  'EQ': apply_comp(lambda x, y: x == y),
}

def eval(ast): return eval_function_by_type[ast['type']](ast)
def operator_node(op, children, version): return { 'type': op, 'children': children, 'version': version }
def num_literal_node(num, version): return { 'type': 'NUM', 'value': num, 'version': version }

def op_by_id(id): return op_by_id_obj[id]

def hex_to_binary(hex_srt):
  res = ''
  for c in hex_srt:
    res = res + simple_hex_to_bin[c]
  return res