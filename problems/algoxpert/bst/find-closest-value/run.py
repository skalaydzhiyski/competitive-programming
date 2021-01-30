#!/usr/bin/python3

# incomplete
def recursive_solve(root, t, best):
  # Rcursive solution is not necessarily better in this case, because we don't want to traverse the tree,
  #   but rather find a single solution which is guaranteed to follow only one branch of the tree
  #       ( this is because of the properties of a BST )
  pass


# The key of a given node is always greater than ALL the keys of nodes in the left subtree !!!
def findClosestValueInBst(root, t):
  best = abs(root.value - t)
  res = root
  current = root
  while current is not None:
    if current.value == t:
      return t
    diff = abs(current.value - t)
    print(diff)
    if diff < best:
      best = diff
      res = root
    if current.value > t:
      # go left 
      current = current.left
    else:
      current = current.right
  return res.value
  


















