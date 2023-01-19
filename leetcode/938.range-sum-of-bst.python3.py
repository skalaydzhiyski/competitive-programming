# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        res = 0
        if low <= root.val <= high:
            res += root.val
        if low < root.val:
            res += self.rangeSumBST(root.left, low, high)
        if high > root.val:
            res += self.rangeSumBST(root.right, low, high)
        return res