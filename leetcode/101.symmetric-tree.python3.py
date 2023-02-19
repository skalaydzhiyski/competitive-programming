# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def invert(root):
            if root is None or (root.left is None and root.right is None):
                return root
            left = invert(root.left)
            right = invert(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root

        def preorder(root, direction):
            if root is None:
                return ""
            res = str(root.val) + direction
            res += preorder(root.left, 'l')
            res += preorder(root.right, 'r')
            return res

        inverted_left = invert(root.left)
        left, right = preorder(inverted_left, ""), preorder(root.right, "")
        return left == right
