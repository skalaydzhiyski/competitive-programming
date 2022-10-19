#!/usr/bin/python3

def preorder(root):
  res = []
  if root is None:
    return []
  res.append(root.value)
  res += preorder(root.left)
  res += preorder(root.right)
  return res


# This is the class of the input binary tree.
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def solve(root):
  if root is None: return
  solve(root.left)
  solve(root.right)
  root.left, root.right = root.right, root.left


def invertBinaryTree(tree):
	solve(tree)


if __name__ == '__main__':
  root = Node(1)
  root.left = Node(2)

  print(preorder(root))
  solve(root)
  print(preorder(root))

