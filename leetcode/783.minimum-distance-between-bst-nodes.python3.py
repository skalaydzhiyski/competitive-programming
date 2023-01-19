# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        inorder = lambda n: inorder(n.left) + [n.val] + inorder(n.right) if n else []
        res = inorder(root)
        return min([
            right - left
            for left, right in zip(res[:-1], res[1:])
        ])