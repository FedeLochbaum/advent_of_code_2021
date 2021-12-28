
from copy import deepcopy
import random

initial_state = lambda pos1, pos2: (2, (int(pos1), 0), (int(pos2), 0)) # Game state = (turnOf, (pos, score), (pos, score), id, level)
won = lambda state, index: state[index][1] >= 21

# A node is an array of the form 
# [ 
#   turn: 0 | 1  
#   [pos, score], # player 0
#   [pos, score]  # player 1
# ]
# graph    = { node => [node] }
# dice = 1 | 2 | 3 

def next_of(prev_state, dice1, dice2, dice3):
  sum = prev_state[0] + dice1 + dice2 + dice3
  next_pos = (10 if (sum % 10 == 0) else sum % 10)
  return (next_pos, prev_state[1] + next_pos)

def next_state_by_dice(node, dice1, dice2, dice3):
  copied = deepcopy(node)
  turnOf = 2 if node[0] == 1 else 1
  return (
    turnOf,
    copied[1] if turnOf == 2 else next_of(copied[1], dice1, dice2, dice3),
    copied[2] if turnOf == 1 else next_of(copied[2], dice1, dice2, dice3),
  )

class Game:
  def __init__(self):
    self.graph = {}
    self.scores = { 'player1': 0, 'player2': 0 }

  def __getitem__(self, node):
    str_node = str(node)
    if (won(node, 1) or won(node, 2)):
      # self.graph[str_node] = []
      self.scores['player1' if won(node, 1) else 'player2'] += 1
      return []
    if str_node not in self.graph:
      self.graph[str_node] = []
      for dice1 in range(1, 4):
        for dice2 in range(1, 4):
          for dice3 in range(1, 4):
            self.graph[str_node].append(next_state_by_dice(node, dice1, dice2, dice3))
    else: print('repito estados')

    return self.graph[str_node]
