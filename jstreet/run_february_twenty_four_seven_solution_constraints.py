#!/Users/darchitect/miniconda3/bin/python3
import numpy as np
from collections import Counter


graph = np.array([
    [0,4,0,0,0,0,0],
    [0,0,6,3,0,0,6],
    [0,0,0,0,0,5,5],
    [0,0,0,4,0,0,0],
    [4,7,0,0,0,0,0],
    [2,0,0,7,4,0,0],
    [0,0,0,0,0,1,0],
])
directions = [(1,0),(-1,0),(0,1),(0,-1)]
start = (5,0)

def check_single_component(graph):
  non_zero = graph[graph != 0].shape[0]
  visited = set()
  component = []
  to_visit = [start]
  while to_visit:
    x,y = to_visit.pop()
    visited.add((x,y))
    component.append(graph[x][y])
    for dx, dy in directions:
      next_ = x + dx, y + dy
      if graph[next_] != 0 and next_ not in visited:
        visited.add(next_)
        to_visit.append(next_)
  return len(component) == non_zero

def check_rows_and_cols_4sum20(graph):
  for i in range(8):
    if graph[:,i].sum() != 20:
      return False
    if graph[i,:].sum() != 20:
      return False
  return True

def check_2x2(graph):
  for i in range(6):
    for j in range(6):
      g = graph[i:i+2, j:j+2]
      #print(g, g.all())
      if g.all():
        return False
    #print()
  return True

def check_full(graph):
  return check_rows_and_cols_4sum20(graph) and check_2x2(graph) and check_single_component(graph)

store = {i:i-1 for i in range(1, 8)}

print(store)
print(check_full(graph))

