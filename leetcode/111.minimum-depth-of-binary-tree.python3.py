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
        if left != 0 and right != 0:
            return min(left, right)
        return left or right
        
