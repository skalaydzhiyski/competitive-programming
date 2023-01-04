import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


def step(corners):
  new = corners.copy()
  new[0] = abs(corners[0] - corners[1])
  new[1] = abs(corners[1] - corners[2])
  new[2] = abs(corners[2] - corners[3])
  new[3] = abs(corners[3] - corners[0])
  return new

def f(corners, verbose=False):
  x = corners
  res = 0
  while x != [0,0,0,0]:
    x = step(x)
    res += 1
    if verbose: print(x)
  return res + 1

def plot_test():
  res = []
  for x in range(1000):
    x = [0,1,2,x]
    fx = f(x)
    print(x, fx)
    res.append(fx)

  plt.plot(res)
  plt.show()

m = defaultdict(list)
max_ = ([], 0)

upper = 7
for a in range(upper):
  for b in range(upper):
    for c in range(upper):
      for d in range(upper):
        x = [a,b,c,d]
        fx = f(x)
        #m[fx].append((x, sum(x)))
        print(x, fx, 'sum = ', sum(x))
#        if fx > max_[1]: max_ = (x, fx)

