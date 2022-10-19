#!/usr/bin/python3


# ---------------- util -----------------------
def inorder(root):
  res = []
  if root is None:
    return []
  res += inorder(root.left)
  res.append(root.value)
  res += inorder(root.right)
  return res

def preorder(root):
  res = []
  if root is None:
    return []
  res.append(root.value)
  res += preorder(root.left)
  res += preorder(root.right)
  return res

def postorder(root):
  res = []
  if root is None:
    return []
  res += postorder(root.left)
  res += postorder(root.right)
  res.append(root.value)
  return res
# ---------------- util -----------------------


# This is an input class. Do not edit.
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def solve(root, res):
  if root is None: return 0

  left = solve(root.left, res)
  right = solve(root.right, res)

  ret = max(left, right)
  s = left + right
  if s > res[0]: res[0] = s
  return ret+1 if ret > 0 else 1



def binaryTreeDiameter(tree):
  res = [-999999999]
  solve(tree, res)
  return res


if __name__ == '__main__':
  root = Node(1)
  root.left = Node(3)
  root.right = Node(2)
  root.left.left = Node(7)
  root.left.right = Node(4)
  root.left.left.left = Node(8)
  root.left.left.left.left = Node(9)
  root.left.right.right = Node(5)
  root.left.right.right.right = Node(6)

  print("input tree:")
  print(preorder(root))
  res = binaryTreeDiameter(root)
  print(res)

