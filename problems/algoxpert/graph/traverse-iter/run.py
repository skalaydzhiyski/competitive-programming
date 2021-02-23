#!/usr/bin/python3
import time 

def log(res, to_visit, current):
  print(f'stack: {to_visit}')
  print(f'visitex: {res}')
  print(f'current: {current}')
  print()


# iterative 
def traverse(g, start, algo='dfs'):
  res = []
  to_visit = [start]
  while len(to_visit):
    current = to_visit.pop() if algo == 'dfs' else to_visit.pop(0)
    res.append(current)
    for node in g[current]:
      if node not in res:
        to_visit.append(node)
    log(res, to_visit, current)
  return res


# recursion
def _dfs(g, node, res):
  res.append(node)
  for x in g[node]:
    dfs(g, x, res)

def _bfs(g, node, res):
  res.append(node)
  for x in g[node]:
    dfs(g, x, res)


n = 9
g = {
    1: [2,3,4],
    2: [],
    3: [],
    4: [5,6],
    5: [7],
    6: [9,8],
    7: [],
    8: [],
    9: [],
}
res = traverse(g, 1)
print(res)

