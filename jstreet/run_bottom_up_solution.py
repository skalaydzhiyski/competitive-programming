import time


def is_valid_square(current, prev):
  res = True
  for idx in range(4):
    next_idx = (idx + 1) % 4
    res &= abs(current[idx] - current[next_idx]) == prev[idx]
  return res

def get_next_options_for(current):
  a = 0
  b = a + current[0]
  small, big = b - current [1], b + current[1]
  rest = [(big, big + current[2])]
  if small >= 0:
    rest.append((small, small + current[2]))
  return [
      [a, b, *r]
      for r in rest
  ]

# main loop
t0 = time.time()
upper = 10000000
max_power = 24
max_ = 2
res = [0,0,0,0]

for p in range(max_power):
  m = 2
  current = [2**p for _ in range(4)]
  while current[-1] <= upper:
    options = get_next_options_for(current)
    valid = [
        opt
        for opt in options
        if is_valid_square(opt, current)
    ]
    if len(valid):
      current = valid[0]
      m += 1
    else:
      current = [x+1 for x in current]
    if m > max_:
      max_ = m
      res = current
      print('current:', current, ', m:', m, ', base', 2**p)
  m = 2

print('\nSOLUTION')
print('(a,b,c,d) =', res, ', res =', sum(res), 'max =', max_)
print('total time', time.time() - t0)
