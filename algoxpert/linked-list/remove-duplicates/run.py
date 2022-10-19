#!/usr/bin/python3

# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

def solve(root):
  res = LinkedList(root.value)
  res_current = res
  prev = root
  current = root.next
  while current is not None:
    if prev.value != current.value:
      res_current.next = LinkedList(current.value)
      res_current = res_current.next
    current = current.next
    prev = prev.next
  return res

def removeDuplicatesFromLinkedList(linkedList):
  return solve(linkedList)



def show(root):
  if root is None:
    return ''
  res = str(root.value) + '->'
  current = root
  while current.next is not None:
    current = current.next
    res += str(current.value) + '->'
  print(res)

if __name__ == '__main__':
  data = [1,1,3,4,4,4,5,6,6]
  root = LinkedList(data[0])
  current = root
  for x in data[1:]:
    current.next = LinkedList(x)
    current = current.next
  show(root)
  show(solve(root))




