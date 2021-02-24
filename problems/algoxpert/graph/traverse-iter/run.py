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
    for node in g[current]:
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
t0 = time()
iter_dfs = traverse(g,1)
print(f'time iter dfs: {time() - t0}')
print(iter_dfs)

t0 = time()
rec_dfs = []
_dfs(g, 1, rec_dfs)
print(f'time rec dfs: {time() - t0}')
print(rec_dfs)
print(rec_dfs == iter_dfs)

# bfs test
t0 = time()
iter_bfs = traverse(g, 1, 'bfs')
print(f'\ntime iter bfs: {time() - t0}')

print(iter_bfs)
t0 = time()
res = []
_bfs(g, 1, [], res)
print(f'time rec bfs: {time() - t0}')
print(res)
print(res == iter_bfs)


