# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        stack = [root]
        while stack:
            current = stack.pop()
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                else:
                    stack.append(current.left)
            else:
                if not current.right:
                    current.right = TreeNode(val)
                else:
                    stack.append(current.right)
        return root


class SolutionRec:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root