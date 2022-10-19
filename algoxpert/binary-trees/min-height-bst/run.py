#!/usr/bin/python3

class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BST(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BST(value)
      else:
        self.right.insert(value)


def preorder(root):
  res = []
  if root is None:
    return []
  res.append(root.value)
  res += preorder(root.left)
  res += preorder(root.right)
  return res


def solve(a, m=None):
  res = []
  if len(a) == 0:
    return []
  m = len(a)//2
  res.append(a[m])
  res += solve(a[:m], m)
  res += solve(a[m+1:], m)
  return res



def minHeightBst(a):
  res = solve(a)
  root = BST(res[0])
  for node in res[1:]:
    root.insert(node)
  return root



array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
minHeightBst(array)



