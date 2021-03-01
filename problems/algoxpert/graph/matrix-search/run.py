#!/Users/architect/anaconda3/bin/python3
from time import sleep

# ---------------------------------------
def show(m, i, j, visited, next_):
  temp = [x.copy() for x in m]
  for i,j in visited:
    temp[i][j] = 'X'
  for order, (i,j) in enumerate(next_):
    temp[i][j] = str(order+1)
  for x in temp:
    print(x)
  print()
# ---------------------------------------


# needed only for "zig zag depth first traversal"
def _get_next(m, i, j, visited, size):
  res = []
  if j+1 < size and not (i, j+1) in visited:
    res.append((i,j+1))
  elif j-1 >= 0 and not (i, j-1) in visited:
    res.append((i,j-1))
  elif i+1 < size and not (i+1, j) in visited:
    res.append((i+1,j))
  elif i-1 >= 0 and not (i-1, j) in visited:
    res.append((i-1,j))
  return res

def get_next(m, i, j, visited, size):
  res = []
  if j+1 < size and not (i, j+1) in visited:
    res.append((i,j+1))
  if j-1 >= 0 and not (i, j-1) in visited:
    res.append((i,j-1))
  if i+1 < size and not (i+1, j) in visited:
    res.append((i+1,j))
  if i-1 >= 0 and not (i-1, j) in visited:
    res.append((i-1,j))
  return res


def search(m, size, algo='dfs'):
  visited = []
  to_visit = [(0,0)]
  while len(to_visit):
    print(to_visit)
    current = to_visit.pop() if algo == 'dfs' else to_visit.pop(0)
    sleep(1)
    visited.append(current)
    next_ = get_next(m, *current, visited, size)
    show(m, *current, visited, next_)
    for x in next_:
      if x not in to_visit:
        to_visit.append(x)
  show(m, *current, visited, [])

size = 4
m = [['_' for _ in range(size)] for _ in range(size)]
print()
# TODO: fix the dfs algo to use only one go to traverse the grid
#search(m, size)
search(m, size, algo='bfs')

