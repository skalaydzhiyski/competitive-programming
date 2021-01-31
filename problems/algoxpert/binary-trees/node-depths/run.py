#!/usr/bin/python3


# This is the class of the input binary tree.
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def solve(root, cur):
  if root is None:
    return 0
  left = solve(root.left, cur+1)
  right = solve(root.right, cur+1)
  res = cur + left + right 
  return res


def nodeDepths(root):
  cur = 0
  res = solve(root, cur)
  print(f"RESULT: {res}:")
  return res
  




























