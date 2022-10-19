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


class Node:
  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent


def leftmost_child(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def rightmost_parent(node):
  current = node
  while current.parent is not None and current.parent.right == current:
    current = current.parent
  return current.parent


def findSuccessor(tree, node):
  if node.right is not None:
    return leftmost_child(node.right)
  return rightmost_parent(node)


if __name__ == '__main__':
  root = Node(1)
  root.left = Node(2)
  root.left.parent = root

  root.right = Node(3)
  root.right.parent = root

  root.left.left = Node(4)
  root.left.left.parent = root.left

  root.left.right = Node(5)
  root.left.right.parent = root.left

  root.left.left.left = Node(6)
  root.left.left.left.parent = root.left.left

  print(inorder(root))
  print(findSuccessor(root, root.left.right).value)



