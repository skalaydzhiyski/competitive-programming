#!/usr/bin/python3
import random
from time import time


def solve(ints):
  ints.append((99999,99999))
  res = []
  new = sorted(ints, key=lambda x: x[0])
  left, right = new[0]
  for n in new[1:]:
    nleft, nright = n
    if right < nleft:
      res.append([left, right])
      left, right = nleft, nright
    else:
      right = max(right, nright)
  return res



def mergeOverlappingIntervals(intervals):
  return solve(intervals)


intervals = [[1,2],[3,5],[4,7],[6,8],[9,10]]
#intervals = [[1,2],[3,5],[4,9],[5,7],[10,12]]
res = mergeOverlappingIntervals(intervals)
print(res)


