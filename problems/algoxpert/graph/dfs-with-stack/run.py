#!/usr/bin/python3
import time 


# iterative implementation
def dfs(g, start):
  res = []
  to_visit = [start]
  while len(to_visit):
    current = to_visit.pop()
    res.append(current)
    for node in g[current]:
      if node not in res:
        to_visit.append(node)
    print(f'stack: {to_visit}')
    print(f'visitex: {res}')
    print(f'current: {current}')
    print()
  return res


# recursive implementation
def _dfs(g, node, res):
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
res = dfs(g, 1)
print(res)

