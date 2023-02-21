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

numbers_used_at_start = graph[graph != 0]
print(numbers_used_at_start)

print(store)
print(check_full(graph))

