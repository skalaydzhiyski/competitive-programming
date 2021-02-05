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


# TODO: Paste base code here

