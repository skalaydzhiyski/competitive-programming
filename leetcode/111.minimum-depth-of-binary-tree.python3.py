# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        current = 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        depth = min(left, right)
        if not left or not right:
            depth = left or right
            
        return current + depth
        
