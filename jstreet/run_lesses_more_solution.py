from time import time
t0 = time()

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


m = ([], 0)
upper = 500
for a in range(upper):
  for b in range(upper):
    for c in range(a, upper):
      for d in range(b, upper):
        x = [a,b,c,d]
        fx = f(x)
        if fx > m[1]:
          m = (x, fx)
          print(x, '\tfx = ', fx)

print(time() - t0)
