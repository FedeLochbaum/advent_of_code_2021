input_path = 'advent_of_code_2021/challenges/Day 21: Dirac Dice/input'

wins_1 = 0; wins_2 = 0
roll = lambda dice: 100 if dice + 1 == 100 else (dice + 1) % 100
initial_state = lambda pos1, pos2: [[int(pos1), 0], [int(pos2), 0]] # Game state = [[pos, score], [pos, score]]
won = lambda state, index: state[index][1] >= 1000

def simulate(state):
  dice = 0; rolls = 0; index = 0
  while(not (won(state, 0) or won(state, 1))):
    roll1 = roll(dice); roll2 = roll(roll1); dice = roll(roll2); rolls +=3
    sum = state[index][0] + roll1 + roll2 + dice
    next_pos = (10 if (sum % 10 == 0) else sum % 10)
    state[index] = [next_pos, state[index][1] + next_pos]
    index = (index + 1) % 2
  print((state[1][1] if won(state, 0) else state[0][1]) * rolls)

with open(input_path) as f: simulate(initial_state(f.readline()[-2], f.readline()[-2]))