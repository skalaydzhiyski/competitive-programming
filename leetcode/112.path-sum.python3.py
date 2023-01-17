# racursive (prefer this for trees!)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val
        if root.left is None and root.right is None:
            return targetSum == 0

        has_left  = self.hasPathSum(root.left, targetSum)
        has_right = self.hasPathSum(root.right, targetSum)
        return has_left or has_right

# iterative
class SolutionIter:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, 0)]
        while stack:
            current, target = stack.pop()

            target += current.val
            if current.left is None and current.right is None:
                if target == targetSum:
                    return True

            if current.left is not None:
                stack.append((current.left, target))
            if current.right is not None:
                stack.append((current.right, target))

        return False