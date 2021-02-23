#!/usr/bin/python3
import time

# ---------------------------------------
def log(m, i, j):
  temp = [x.copy() for x in m]
  temp[i][j] = 'X'
  for x in temp:
    print(x)
  print(f'value: {m[i][j]}\t idx: ({i,j})\n')
# ---------------------------------------


def solve(m):
  res = []
  visited = [[False]*len(m[0]) for _ in range(len(m))]
  for x in visited: print(x)
  print()
  for i in range(len(m)):
    for j in range(len(m[0])):
      if visited[i][j]:
        continue
      explore(m, i, j, visited, res)
  print()
  for x in visited: print(x)
  return res

def get_unvisited(m, i,j, visited):
  res = []
  if i>0 and not visited[i-1][j]:
    res.append((i-1,j))
  if i<len(m)-1 and not visited[i+1][j]:
    res.append((i+1,j))
  if j>0 and not visited[i][j-1]:
    res.append((i,j-1))
  if j<len(m[0])-1 and not visited[i][j+1]:
    res.append((i,j+1))
  return res

def explore(m, i, j, visited, res):
  l = 0
  to_visit = [(i,j)]
  while len(to_visit):
    pos = to_visit.pop(0)
    i,j = pos
    if visited[i][j]:
      continue
    visited[i][j] = True
    if m[i][j] == 0:
      continue
    # here we haven't visited the node and the value is 1
    l += 1
    next_ = get_unvisited(m, i,j, visited)
    for n in next_:
      to_visit.append(n)
  if l > 0:
    res.append(l)



# main solution 
def riverSizes(matrix):
  return solve(matrix)

m =[
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]
print(riverSizes(m))
