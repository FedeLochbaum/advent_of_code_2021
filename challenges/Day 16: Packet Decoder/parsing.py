input_path = 'advent_of_code_2021/challenges/Day 16: Packet Decoder/test'
from utils import hex_to_binary

def operator_node(op, children, version): return { 'type': 'OP', 'op': op, 'chilcren': children, 'version': version }
def num_literal_node(num, version): return { 'type': 'NUM', 'value': num, 'version': version }

def op_by_id(id): return id #TODO

def consume_packet_by(id):
  if (id == '100'): return consume_literal_value
  return consume_operator

def consume_number_in_range(buffer, i, j):
  return int(buffer[i:j], 2)

def consume_operator(buffer, i, version, id):
  print('version, id: ', version, id)
  sub_packets = []
  if buffer[i] == '0':
    total_length_in_bits = consume_number_in_range(buffer, i+1, i+16)
    print('voy por total_length: ', total_length_in_bits)
    i+=16
    j=0
    while (j != total_length_in_bits):
      ast, _i = consume_packet(buffer, i)
      print('consumi: ', _i)
      sub_packets.append(ast)
      j+=(_i-i)
      i=_i
  else:
    number_of_sub_packets = consume_number_in_range(buffer, i+1, i+12)
    print('voy por number_of_sub_packets: ', number_of_sub_packets)
    i+=12
    for _ in range(number_of_sub_packets):
      ast, _i = consume_packet(buffer, i)
      sub_packets.append(ast)
      i=_i

  return operator_node(op_by_id(id), sub_packets, version), i

# todo gud
def consume_literal_value(buffer, i, version, _):
  print('version, id: ', version)
  while(buffer[i] == '0'): i+=1
  number = ''
  while(True):
    header = buffer[i]
    number = number + buffer[i+1:i+5]
    i+=5
    if (header == '0'): break
  print('numerin: ',number, int(number, 2))
  return num_literal_node(int(number, 2), version), i

# TODO: Goes consuming on demand the filee with a buffer
input = hex_to_binary(open(input_path).readline())

def consume_packet(buffer, i):
  version = buffer[i:i+3]
  id = buffer[i+3:i+6]
  return consume_packet_by(id)(buffer, i+6, int(version, 2), int(id, 2))

ast = consume_packet(input, 0)

# binary_string = binascii.unhexlify(string)

# print(binary_string)