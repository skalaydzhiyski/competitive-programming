# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        flag = True
        levels = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels.append(level)
            flag = not flag

        return [
            reversed(level) if idx % 2 else level
            for idx, level in enumerate(levels)
        ]
