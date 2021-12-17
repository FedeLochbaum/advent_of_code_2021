input_path = 'advent_of_code_2021/challenges/Day 16: Packet Decoder/input'
from utils import hex_to_binary, operator_node, num_literal_node, op_by_id, eval

def consume_packet_by(id): return (consume_literal_value if id == '100' else consume_operator)
def consume_number_in_range(buffer, i, j): return int(buffer[i:j], 2)

def consume_operator(buffer, i, version, id):
  sub_packets = []
  if buffer[i] == '0':
    total_length_in_bits = consume_number_in_range(buffer, i+1, i+16)
    i+=16; j=0
    while (j != total_length_in_bits):
      ast, _i = consume_packet(buffer, i)
      sub_packets.append(ast)
      j+=(_i-i)
      i=_i
  else:
    number_of_sub_packets = consume_number_in_range(buffer, i+1, i+12)
    i+=12
    for _ in range(number_of_sub_packets):
      ast, _i = consume_packet(buffer, i)
      sub_packets.append(ast)
      i=_i

  return operator_node(op_by_id(id), sub_packets, version), i

def consume_literal_value(buffer, i, version, _):
  number = ''
  while(True):
    header = buffer[i]
    number = number + buffer[i+1:i+5]
    i+=5
    if (header == '0'): break
  return num_literal_node(int(number, 2), version), i

def consume_packet(buffer, i):
  version = buffer[i:i+3]
  id = buffer[i+3:i+6]
  return consume_packet_by(id)(buffer, i+6, int(version, 2), int(id, 2))

input = hex_to_binary(open(input_path).readline())
ast, i = consume_packet(input, 0)
print(eval(ast))