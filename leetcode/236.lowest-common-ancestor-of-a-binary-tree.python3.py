# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        valid = (p,q)
        if (left in valid and right in valid) or\
            (root in valid and left in valid) or\
            (root in valid and right in valid):
            return root

        if left == p or left == q:
            return left
        if right == p or right == q:
            return right

        return left if left is not None else right
