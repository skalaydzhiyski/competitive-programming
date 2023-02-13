from math import prod

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        N = len(nums)
        total = sum(nums)
        res = current = sum(map(prod, zip(range(N), nums)))
        for i in range(N):
            last = nums[-(i+1)]
            rem = total - last
            current = current - (N-1)*last + rem
            if current > res:
                res = current
        return res