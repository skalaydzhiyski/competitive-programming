# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution(object):
  def to_num(self, l):
    res, p = 0, 0
    while l:
      res += l.val * (10**p)
      p += 1
      l = l.next
    return res

  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    s = self.to_num(l1) + self.to_num(l2)
    if s == 0: return ListNode()

    digits = []
    while s > 0:
      digits.append(s%10)
      s /= 10

    current = root = ListNode(digits[0])
    for d in digits[1:]:
      node = ListNode(d)
      current.next = node
      current = current.next
    return root

