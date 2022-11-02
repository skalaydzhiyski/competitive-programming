class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        mi = 0
        res = []
        left, right = 0, N-1
        while len(res) < N:
            if abs(nums[left]) <= nums[right]:
                c = nums[right]
                right -= 1
            else:
                c = nums[left]
                left += 1
            res.append(c**2)
        return res[::-1]
