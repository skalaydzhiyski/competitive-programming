# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def solve(root, min_, max_):
            nonlocal res
            if root is None:
                return 0
            if root.val > max_:
                max_ = root.val
            if root.val < min_:
                min_ = root.val
            current = abs(min_ - max_)
            if current > res:
                res = current
            solve(root.left, min_, max_)
            solve(root.right, min_, max_)
        solve(root, 999999, -9999999)
        return res
