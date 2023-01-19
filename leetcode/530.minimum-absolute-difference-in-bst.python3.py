# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder = lambda n: inorder(n.left) + [n.val] + inorder(n.right) if n else []
        res = inorder(root)
        return min([
            right - left
            for left, right in zip(res[:-1], res[1:])
        ])


class SolutionRec:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = self.min_ = 10**5 + 1
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.min_ = min(self.min_, abs(root.val - self.prev))
            self.prev = root.val
            inorder(root.right)
        inorder(root)
        return self.min_