from copy import deepcopy
empty_hallway = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

initial_state = lambda a, b, c, d: (a, b, c, d, empty_hallway.copy())
step_cost_by = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
room_pos = { 'A': 2, 'B': 4, 'C': 6, 'D': 8 }
goal = { 'A': 0, 'B': 1, 'C': 2, 'D': 3 }

is_goal = lambda state: state == [['A', 'A', 'A', 'A'], ['B', 'B', 'B', 'B'], ['C', 'C', 'C', 'C'], ['D', 'D', 'D', 'D'], empty_hallway]

def hallway_actions_by_index(state, index, elem, steps_until_hallway, from_pos):
  actions = []
  if (not index in [room_pos['A'], room_pos['B'], room_pos['C'], room_pos['D']]):
    _state = deepcopy(state)
    _state[4][index] = elem
    cost = (steps_until_hallway + abs(from_pos - index)) * step_cost_by[elem]
    actions.append((cost, _state))
  actions = actions + case_to_enter_on_room(state, index, elem, steps_until_hallway, from_pos)
  return actions

def case_to_enter_on_room(current_state, hallway_index, elem, steps_until_hallway, from_pos):
  all_like_me = all(map(lambda x: x == elem, current_state[goal[elem]]))
  if (hallway_index == room_pos[elem] and all_like_me):
    steps_to_enter = abs(len(current_state[goal[elem]]) - 4)
    cost = (steps_until_hallway + abs(from_pos - hallway_index) + steps_to_enter) * step_cost_by[elem]
    __state = deepcopy(current_state)
    __state[goal[elem]].insert(0, elem)
    return [(cost, __state)]
  else: return []

def hallway_actions(state):
  actions = []
  for pos, elem in enumerate(state[4]):
    if elem != '.':
      copied_state = deepcopy(state)
      copied_state[4][pos] = '.' # Modified copied
      if all(map(lambda x: x == elem, copied_state[goal[elem]])):
        steps_to_enter = abs(len(copied_state[goal[elem]]) - 4)
        cost = (abs(pos - room_pos[elem]) + steps_to_enter) * step_cost_by[elem]
        copied_state[goal[elem]].insert(0, elem)
        actions = actions + [(cost, copied_state)]
  return actions

def actions_on_room(state, room_index, room):
  actions = []
  if len(state[room_index]) == 0: return []
  steps_until_hallway = abs(len(state[room_index]) - 4) + 1
  copied_state = deepcopy(state)
  head = copied_state[room_index].pop(0) # Modified copied

  for i in reversed(range(room_pos[room])):
    if (state[4][i] != '.'): break # case when there is another Letter
    actions = actions + hallway_actions_by_index(copied_state, i, head, steps_until_hallway, room_pos[room])

  for i in range(room_pos[room] + 1, len(empty_hallway)):
    if (state[4][i] != '.'): break # case when there is another Letter
    actions = actions + hallway_actions_by_index(copied_state, i, head, steps_until_hallway, room_pos[room])

  return actions
class Game:
  def __init__(self):
    self.graph = {}

  def __getitem__(self, node):
    str_node = str(node)
    if is_goal(node): return []
    if str_node not in self.graph:
      self.graph[str_node] = (
        actions_on_room(node, 0, 'A') +
        actions_on_room(node, 1, 'B') +
        actions_on_room(node, 2, 'C') +
        actions_on_room(node, 3, 'D') +
        hallway_actions(node)
      )

    return self.graph[str_node]