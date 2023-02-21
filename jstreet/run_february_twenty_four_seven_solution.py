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

def check_single_component():
  global graph
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

def check_valid_rows_cols():
  global graph
  for i in range(7):
    col = graph[:,i]
    if col[col != 0].shape[0] > 4:
      return False
  for i in range(7):
    row = graph[i,:]
    if row[row != 0].shape[0] > 4:
      return False
  return True

def check_2x2():
  global graph
  for i in range(6):
    for j in range(6):
      g = graph[i:i+2, j:j+2]
      #print(g, g.all())
      if g.all():
        return False
    #print()
  return True
  

store = {i:i for i in range(1,8)}
numbers_used_at_start = graph[graph != 0]
print(store)
print(numbers_used_at_start)

for number in numbers_used_at_start:
  store[number] -= 1
store = {k:v for k,v in store.items() if v != 0}
print(store)

def solve(store):
  global graph
  print("start")
  for i in range(7):
    for j in range(7):
      if graph[i][j] == 0:
        for k,v in store.items():
          if v != 0:
            graph[i][j] = k
            store[k] -= 1
            print(graph)
            print()
            if check_2x2() and check_valid_rows_cols():
              solve(store)
            graph[i][j] = 0
            store[k] += 1
        print("no match")
        return

  print('end')
  print(graph)

solve(store)


