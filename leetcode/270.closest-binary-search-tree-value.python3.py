# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        stack = [root]
        while stack:
            current = stack.pop()
            if abs(current.val - target) < abs(res - target):
                res = current.val
            if current.left and target < current.val:
                stack.append(current.left)
            elif current.right and target > current.val:
                stack.append(current.right)
        return res


class SolutionRec:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def solve(root, target, res):
            if root is None:
                return res
            if abs(root.val - target) < abs(res - target):
                res = root.val
            if target < root.val:
                return solve(root.left, target, res)
            return solve(root.right, target, res)
        return solve(root, target, root.val)
