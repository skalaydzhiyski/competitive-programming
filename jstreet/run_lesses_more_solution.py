import pandas as pd
from itertools import permutations
import time

def step(corners):
  return [
    abs(left - right)
    for left, right in zip(corners, corners[1:] + [corners[0]])
  ]

def f(corners, verbose=False):
  x = corners
  res = 0
  while any(x):
    x = step(x)
    res += 1
    if verbose: print(x)
  return res + 1

def get_valid(x):
  rev = list(reversed(x))
  valid = []
  for idx in range(len(x)):
    valid.append(x[idx:] + x[:idx])
    valid.append(rev[idx:] + rev[:idx])
  return valid

def get_max_perm(x):
  res = []
  valid = get_valid(x)
  perm = [list(p) for p in permutations(x) if list(p) not in valid]
  for p in perm:
    if f(p) > f(res):
      res = p
  return res


t0 = time.time()
upper = 50
m = 0

res_data = []
#a = 0
db, dc = 0,0
for a in range(upper):
  for b in range(upper):
    #for c in range(b+db, upper):
    for c in range(upper):
      #for d in range(c+dc, upper):
      for d in range(upper):
        x = [a,b,c,d]
        r = (abs(a-b), abs(b-c), abs(c-d), abs(d-a))
        fx = f(x)
        if fx > m:
          m = fx
          dc = abs(c-d)
          db = abs(b-c)
          print('(a,b,c,d) =', x, '\tfx = ', fx, '\tdistances =', r, '\tcurrent max =', m, 'MAX !')
       # else: print('(a,b,c,d) =', x, '\tfx = ', fx, '\tdistances =', r, '\tcurrent max =', m)
        res_data.append((x, r, fx, m))
        #time.sleep(.01)
print(time.time() - t0)

res = pd.DataFrame(res_data, columns=['tuple', 'dist', 'fx', 'm'])
del res_data

