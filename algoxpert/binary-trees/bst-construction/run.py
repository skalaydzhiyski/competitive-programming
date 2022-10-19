#!/usr/bin/python3


def inorder(root):
  if root is None:
    return
  print(root.value)
  inorder(root.left)
  inorder(root.right)



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


def custom_testing():
  #root = reset()
  root = Node(10)
  root.insert(5)
  root.insert(15)
  root.insert(2)
  root.insert(6)
  root.insert(13)
  root.insert(22)
  root.insert(1)
  root.insert(14)
  root.insert(12)
  print('-'*50)

  print(inorder(root))
  print('-'*50)

  # insert
  t = 4
  root.insert(t)
  print(f'contains {t}? {root.contains(t)}')
  #print(inorder(root))

  print('-'*50)


  # remove
  t = 4
  print(f'removing {t}')
  root.remove(t)
  print(f'contains {t}? {root.contains(t)}')
  print()
  print(inorder(root))
  print('-'*50)

  t = 10
  print(f'removing {t}')
  root.remove(t)
  print(f'contains {t}? {root.contains(t)}')
  print()
  print(inorder(root))
  print('-'*50)

  t = 15
  print(f'removing {t}')
  root.remove(t)
  print(f'contains {t}? {root.contains(t)}')
  print()
  print(inorder(root))
  print('-'*50)

def parse_test(root, test):
  for t in test:
    arg = t['arguments'][0]
    meth = t['method']
    inorder(root)
    print(meth, arg)
    Node.__dict__[meth](root, arg)
	

if __name__ == '__main__':
  root = Node(10)
  test = [
    {"arguments": [5], "method": "insert"},
    {"arguments": [15], "method": "insert"},
    {"arguments": [5], "method": "remove"},
    {"arguments": [15], "method": "remove"},
    {"arguments": [10], "method": "remove"}
  ]
  inorder(root)
  parse_test(root, test)
  inorder(root)
