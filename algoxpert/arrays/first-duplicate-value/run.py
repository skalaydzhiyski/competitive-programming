#!/usr/bin/python3

def firstDuplicateValue(a):
  d = {x:0 for x in a}
  for x in a:
    d[x] += 1
    if d[x] == 2:
      return x
  return -1


print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))




