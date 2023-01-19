# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def solve(root, low, high):
            nonlocal res
            if root is None:
                return
            if low <= root.val <= high:
                res += root.val
            if low < root.val:
                solve(root.left, low, high)
            if high > root.val:
                solve(root.right, low, high)

        solve(root, low, high)
        return res