# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def __repr__(self):
#         return str(self.val)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        current = head
        pos = 1
        while pos < left:
            prev = current
            current = current.next
            pos += 1
        s, e = prev, current
        prev = None
        while pos <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            pos += 1
        if current is not None: e.next = current
        if s is not None: s.next = prev
        else: head = prev
        return head

