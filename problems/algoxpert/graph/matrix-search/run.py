#!/Users/architect/anaconda3/bin/python3

# ---------------------------------------
def show(m, i, j, visited):
  temp = [x.copy() for x in m]
  for i,j in visited:
    temp[i][j] = 1
  for x in temp:
    print(x)
  print()
# ---------------------------------------


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
    current = to_visit.pop() if algo == 'dfs' else to_visit.pop(0)
    show(m, *current, visited)
    visited.append(current)
    next_ = get_next(m, *current, visited, size)
    for x in next_:
      if x not in to_visit:
        to_visit.append(x)
  show(m, *current, visited)

size = 4
m = [[0 for _ in range(size)] for _ in range(size)]
print()
# TODO: fix the dfs algo to use only one go to traverse the grid
search(m, size)
#search(m, size, algo='bfs')

