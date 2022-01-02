from copy import deepcopy
empty_hallway = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

initial_state = lambda a, b, c, d: (a, b, c, d, empty_hallway.copy())
step_cost_by = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
room_pos = { 'A': 3, 'B': 5, 'C': 7, 'D': 9}
goal = { 'A': 0, 'B': 1, 'C': 2, 'D': 3 }

is_goal = lambda state: state == (['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D'], empty_hallway)

def hallway_actions_by_index(state, index, elem, steps_until_hallway, from_pos):
  actions = []
  new_hallway = state[4].copy()
  new_hallway[index] = elem
  cost = (steps_until_hallway + abs(from_pos - index)) * step_cost_by[elem]
  _state = [state[0].copy(), state[1].copy(), state[2].copy(), state[3].copy(), new_hallway]
  actions.append((cost, _state))
  actions = actions + case_to_enter_on_room(index, state, elem, steps_until_hallway, from_pos)
  return actions

def case_to_enter_on_room(hallway_index, current_state, elem, steps_until_hallway, from_pos):
  all_mines = all(map(lambda x: goal[x] == goal[elem], current_state[goal[elem]]))
  if (hallway_index == room_pos[elem] and len(current_state[goal[elem]]) > 0 and all_mines):
    steps_to_enter = 1 if len(current_state[goal[elem]]) == 1 else 2
    _hallway = current_state[4].copy()
    cost = (steps_until_hallway + (from_pos - hallway_index) + steps_to_enter) * step_cost_by[elem]
    __state = [current_state[0].copy(), current_state[1].copy(), current_state[2].copy(), current_state[3].copy(), _hallway]
    __state[goal[elem]].append(elem)
    return [(cost, __state)]
  else: return []

def hallway_actions(state):
  actions = []
  for pos, elem in enumerate(state[4]):
    if elem != '.':
      copied_state = deepcopy(state)
      copied_state[4][pos] = '.' # Modified copied
      for i in reversed(range(pos)):
        if (state[4][i] != '.'): break # case when there is another Letter
        actions = actions + hallway_actions_by_index(copied_state, i, elem, 0, pos)

      for i in range(pos + 1, len(empty_hallway)):
        if (state[4][i] != '.'): break # case when there is another Letter
        actions = actions + hallway_actions_by_index(copied_state, i, elem, 0, pos)
  return actions

def actions_on_room(state, room_index, room):
  actions = []
  if len(state[room_index]) == 0: return []
  steps_until_hallway = 1 if len(state[room_index]) == 2 else 2
  copied_state = deepcopy(state)
  head = copied_state[room_index].pop() # Modified copied

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
    if str_node not in self.graph:
      self.graph[str_node] = (
        actions_on_room(node, 0, 'A') +
        actions_on_room(node, 1, 'B') +
        actions_on_room(node, 2, 'C') +
        actions_on_room(node, 3, 'D') +
        hallway_actions(node)
      )

    return self.graph[str_node]

# node => (cost, node)