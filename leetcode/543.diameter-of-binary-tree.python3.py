# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_ = -1
        def dfs(root):
            nonlocal max_
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            current = 1 + left + right
            if current > max_:
                max_ = current
            return max(left, right) + 1
        dfs(root)
        return max_ - 1
