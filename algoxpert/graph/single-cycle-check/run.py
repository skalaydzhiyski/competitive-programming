#!/usr/bin/python3

# This problem has wrong description, since we're not accounting for all the possible starting points here 
#   but, rather brute forcily we set the starting index to 0 ignoring the description where it says ANY starting index.
def solve(a):
  current = 0
  m = 0
  while m < len(a):
    if m > 0 and current == 0:
      return False
    m += 1
    j = a[current]
    # using the built-in Python negative indexing here
    current = (current + j) % len(a)
  return current == 0


def hasSingleCycle(a):
  return solve(a)


#a = [2,3,1,-4,-4,2]
#a = [0,1,0,1]
#a = [-26, 1, 2, 3, 4]
a = [1,1,1,1,-250]
print(hasSingleCycle(a))

