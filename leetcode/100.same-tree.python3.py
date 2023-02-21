# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited_left, visited_right = set(), set()
        to_visit = deque([ (p, q) ])
        while to_visit:
            pnode, qnode = to_visit.popleft()
            if not pnode and not qnode:
                continue
            if (pnode and not qnode) or (not pnode and qnode) or pnode.val != qnode.val:
                return False
            to_visit.append((pnode.left, qnode.left))
            to_visit.append((pnode.right, qnode.right))
        return True
