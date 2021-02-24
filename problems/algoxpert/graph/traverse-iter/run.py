#!/usr/bin/python3
from time import time


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
    neigh = g[current] if algo == 'bfs' else list(reversed(g[current]))
    for node in neigh:
      if node not in res:
        to_visit.append(node)
    #log(res, to_visit, current)
  return res


# recursion
def _dfs(g, node, res):
  res.append(node)
  for x in g[node]:
    _dfs(g, x, res)

def _bfs(g, node, to_visit, res):
  res.append(node)
  to_visit += g[node]
  for x in to_visit:
    current = to_visit.pop(0)
    _bfs(g, current, to_visit, res)



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
iter_dfs = traverse(g,1)
print(iter_dfs)
rec_dfs = []
_dfs(g, 1, rec_dfs)
print(rec_dfs)
print(rec_dfs == iter_dfs)

# bfs test
iter_bfs = traverse(g, 1, 'bfs')
print(iter_bfs)
res = []
_bfs(g, 1, [], res)
print(res)
print(res == iter_bfs)


