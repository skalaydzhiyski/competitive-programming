# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        left, right = head, head.next
        while right is not None:
            while right is not None and left.val == right.val:
                right = right.next
            left.next = right
            left = left.next
            if right is not None:
                right = right.next
        return head
