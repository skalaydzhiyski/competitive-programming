import numpy as np
from llist import dllist, dllistnode


def swap(die, x, y):
  die[x], die[y] = die[y], die[x]

def step(die, direction):
  res = die.copy()
  center, bottom = (1,1), (0,0)
  left, right, up, down = (1,0), (1,2), (0,1), (2,1)
  if direction == (0, -1):
    swap(res, left, bottom)
    swap(res, center, left)
    swap(res, center, right)
  elif direction == (0, 1):
    swap(res, right, bottom)
    swap(res, center, right)
    swap(res, center, left)
  elif direction == (-1, 0):
    swap(res, up, bottom)
    swap(res, center, up)
    swap(res, center, down)
  elif direction == (1,0):
    swap(res, down, bottom)
    swap(res, center, down)
    swap(res, center, up)
  return res

def get_unvisited_adjacent(pos, visited):
  positions = [
    (pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]),
    (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)
  ]
  res = [
    (x,y) for x,y in positions
    if 0 <= x <= 5
    and 0 <= y <= 5
    and not visited[(x,y)]
  ]
  return res


grid = np.array([
    [57,33,132,268,492,732],
    [81,123,240,443,353,508],
    [186,42,195,704,452,228],
    [-7,2,357,452,317,395],
    [5,23,-4,592,445,620],
    [0,77,32,403,337,452]
])
die = np.array([
  ['c','d','-'],
  ['e','a','f'],
  ['-','b','-'],
], dtype='<U3')
face = (1,1)

pos = (5,0)
target = 732
N = 1
S = 0

visited = grid.copy()
visited.fill(False)
visited[pos] = True
to_visit = get_unvisited_adjacent(pos, visited)
path = [(pos, die, S, visited)]

placeholders = 'abcdef'
while grid[pos] != target:
  next_pos = to_visit.pop()
  value = grid[next_pos]

  direction = (next_pos[0]-pos[0], next_pos[1]-pos[1])
  next_die_state = step(die, direction)

  # NOTE: Typical DFS might not work here since we need to actively backtrack and reverse the state
  #   1. if a neighbor can be next (matches the rule) we append to the state stack
  #   2. else if there are NO neighbors to matc the rule, we revert the current step and pop it off the state stack
  #   3. we still keep track of to_visit at every state stack frame and when rolling back we remove from the stack frame's to_visit the node we are coming back from !  
  N += 1


