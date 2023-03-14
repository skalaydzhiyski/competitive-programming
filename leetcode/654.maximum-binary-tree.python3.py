# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(nums, root):
            if root is None:
                if len(nums):
                    m = max(nums)
                    idx = nums.index(m)
                    root = TreeNode(m)
                else:
                    return None
            root.left = solve(nums[:idx], None)
            root.right = solve(nums[idx+1:], None)
            return root
        return solve(nums, None)
