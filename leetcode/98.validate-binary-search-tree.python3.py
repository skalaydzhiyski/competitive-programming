# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = lambda node: inorder(node.left) + [node.val] + inorder(node.right) if node else []
        nodes = inorder(root)
        return all([
            left < right
            for left, right in zip(nodes[:-1], nodes[1:])
        ])
