# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return min([
            abs(left-right)
            for left, right in zip(nodes[:-1], nodes[1:])
        ])
