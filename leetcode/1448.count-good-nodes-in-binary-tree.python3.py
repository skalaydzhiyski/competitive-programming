# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_):
            if root is None:
                return 0

            current = 0
            if root.val >= max_:
                max_ = root.val
                current = 1

            if root.left is not None:
                current += dfs(root.left, max_)
            if root.right is not None:
                current += dfs(root.right, max_)
            return current

        return dfs(root, -999999999)