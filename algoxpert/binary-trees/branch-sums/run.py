#!/usr/bin/python

class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def solve(root, s, res):
  if root is None:
    return 
  s += root.value
  if root.left is None and root.right is None:
    res += s
  solve(root.left, s, res)
  solve(root.right, s, res)

def branchSums(root):
  res = []
  solve(root, 0, res)
  return res


if __name__ == "__main__":
  # test the tree here (didn't add testing code since tree init is a pain in the a)
  pass


