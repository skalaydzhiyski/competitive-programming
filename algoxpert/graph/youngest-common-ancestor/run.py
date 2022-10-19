#!/usr/bin/python3


# This is an input class. Do not edit.
class AncestralTree:
  def __init__(self, name):
    self.name = name 
    self.ancestor = None


def height(node, root):
  res = 0
  current = node
  while current.name != root.name:
    res += 1
    current = current.ancestor
  return res


def solve(root, node1, node2):
  h1 = height(node1, root)
  h2 = height(node2, root)
  if h1 > h2:
    return backtrack(node1, node2, h1-h2)
  else:
    return backtrack(node2, node1, h2-h1)


def backtrack(low, high, diff):
  while diff > 0:
    low = low.ancestor
    diff -=1
  while low != high:
    low = low.ancestor
    high = high.ancestor
  return high


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
  return solve(topAncestor, descendantOne, descendantTwo)



