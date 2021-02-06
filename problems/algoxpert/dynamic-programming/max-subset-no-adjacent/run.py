#!/usr/bin/python3

def solve(a):
  if len(a) <= 2: return max(a + [0])
  last = a[0]
  res = max(a[1], last)
  for i,x in enumerate(a[2:]):
    i = i+2
    current = max(res, x+last)
    last = res
    res = current
  return res


def maxSubsetSumNoAdjacent(array):
  return solve(array)


a = [7,10,12,7,9,14]
print(maxSubsetSumNoAdjacent(a))

