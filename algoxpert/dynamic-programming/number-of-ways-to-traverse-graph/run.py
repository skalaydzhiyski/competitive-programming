#!/usr/bin/python3



def solve(width, height):
  # if any of the width or height is 1 then we know we are at a row/column respectively.
  if width == 1 and height == 1:
    return 1
  return solve(width-1, height) + solve(width, height-1)


def numberOfWaysToTraverseGraph(width, height):
  return solve(width, height)

res = numberOfWaysToTraverseGraph(4, 3)
print(res)


