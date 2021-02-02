#!/usr/bin/python3

class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def validateBst(root):
  # Write your code here.
  pass


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current = self
    while True:
      if value < current.value:
        if current.left is None:
          current.left = Node(value)
          break
        else:
          current = current.left
      else:
        if current.right is None:
          current.right = Node(value)
          break
        else:
          current = current.right
    return self

  def contains(self, value):
    current = self
    while current is not None:
      if value < current.value:
        current = current.left
      elif value > current.value:
        current = current.right
      else:
        return True
    return False

  def _find_min_value(self):
    new = self
    while new.left is not None: new = new.left
    return new.value

  def remove(self, value, prev=None):
    current = self
    while current is not None:
      if value < current.value:
        prev = current
        current = current.left
      elif value > current.value:
        prev = current
        current = current.right
      else:
        print('found')

        if current.left is not None and current.right is not None:
          print('case left AND right')
          current.value = current.right._find_min_value()
          current.right.remove(current.value, current)

        elif prev is None:
          if current.left is not None:
            # just copy everything of left to current (root)
            current.value = current.left.value
            current.right = current.left.right
            current.left = current.left.left
          elif current.right is not None:
            # just copy everything of right to current (root)
            current.value = current.right.value
            current.left = current.right.left
            current.right = current.right.right
          else: 
            pass

        # at this point we know we have only 1 subtrree (either to the left or right of current)
        #  so 1. determine which subtree needs replacing and set it to the current's subtree
        #     (note it doesn't matter which one since both will be smaller/greater than 
        #      the parent, thus retaining the BSTs invariant)
        elif prev.left == current:
          prev.left = current.left if current.left is not None else current.right
        elif prev.right == current:
          prev.right = current.left if current.left is not None else current.right

        else:
          # case leaf
          if prev.left == current:
            prev.left = None
          else:
            prev.right = None
        break
    return self

def parse_test(root, test):
  for t in test:
    arg = t['arguments'][0]
    meth = t['method']
    Node.__dict__[meth](root, arg)

# TODO: generate inorder string repr of the traversal
def solve(root, low, high):
  if root is None:
    return True
  if root.value >= low and root.value < high:
    return solve(root.left, low, root.value) & solve(root.right, root.value, high)
  return False

class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def validateBst(root):
  res = solve(root, -9999999, 999999)
  print('result:')
  print(res)
  return res


if __name__ == '__main__':
  root = Node(10)
  test = [
    {"arguments": [5], "method": "insert"},
    {"arguments": [15], "method": "insert"},
    {"arguments": [5], "method": "insert"},
    {"arguments": [2], "method": "insert"},
    {"arguments": [13], "method": "insert"},
    {"arguments": [22], "method": "insert"},
    {"arguments": [10], "method": "insert"},
    {"arguments": [1], "method": "insert"},
    {"arguments": [14], "method": "insert"},
  ]
  parse_test(root, test)
  #print(validateBst(root))

  # new where we have a wrong entry in the tree 
  print('BAD')
  root = Node(10)
  root.left = Node(5)
  root.left.right = Node(10)
  root.right = Node(15)
  print(validateBst(root))

  print('-' * 50)
  print('GOOD')
  root = Node(10)
  root.left = Node(5)
  root.right = Node(15)
  root.right.left = Node(10)
  #print(validateBst(root))

  print('-' * 50)
  print('GOOD')
  root = Node(10)
  root.left = Node(5)
  root.right = Node(10)
  root.right.right = Node(15)
  print(validateBst(root))

  


