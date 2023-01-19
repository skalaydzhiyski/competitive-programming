# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([root])
        while q:
            current = 0
            for _ in range(len(q)):
                node = q.popleft()
                current += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res = current
        return res
