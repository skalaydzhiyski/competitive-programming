# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def solve(root, min_, max_):
            nonlocal res
            if root is None:
                return 0
            if root.val > max_:
                max_ = root.val
            if root.val < min_:
                min_ = root.val
            current = abs(min_ - max_)
            if current > res:
                res = current
            solve(root.left, min_, max_)
            solve(root.right, min_, max_)
        solve(root, 999999, -9999999)
        return res


# Original Solution
class SolutionOrig:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        paths = []
        def solve(root, path):
            current = path + [root.val]
            if not root.left and not root.right:
                paths.append(current)
                return
            if root.left:
                solve(root.left, current)
            if root.right:
                solve(root.right, current)
        def max_diff(path):
            max_ = -1
            n = len(path)
            for i in range(n):
                for j in range(i+1, n):
                    max_ = max(max_, abs(path[i] - path[j]))
            return max_
        solve(root, [])
        return max(map(max_diff, paths))

