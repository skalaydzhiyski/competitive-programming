#!/usr/bin/python3

# My Solution
def solve(a):
  if len(a) == 1: return 0
  return sum(a) + solve(a[:-1]) 

def myminimumWaitingTime(a):
  a.insert(0, 0)
  return solve(sorted(a)[:-1])


# AlgoExpert solution
def minimumWaitingTime(a):
  a.sort()
  total = 0
  for idx, duration in enumerate(a):
    left = len(a) - (idx+1)
    total += duration * left
    print(idx, duration, left, total)
  return total


a = [3,2,1,2,6]
res = minimumWaitingTime(a)
print(res)

