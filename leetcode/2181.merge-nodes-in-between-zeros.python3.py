# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = 0
        iterator = head
        sent = iterator
        while head.next:
            head = head.next
            if head.val != 0:
                current += head.val
            else:
                node = ListNode(current)
                iterator.next = node
                iterator = iterator.next
                current = 0
        return sent.next
        
