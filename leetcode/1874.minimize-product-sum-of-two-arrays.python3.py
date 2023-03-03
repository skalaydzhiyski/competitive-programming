class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        return sum([
            left * right
            for left, right in zip(reversed(sorted(nums1)), sorted(nums2))
        ])
