class Solution:
    def findMaxAverage(self, nums, k):
        N = len(nums)
        left, right = 0, k
        s = float(sum(nums[:k])) 
        res = s / k
        while right < N:
            s -= nums[left]
            s += nums[right]
            m = s / k
            if m > res:
                res = m
            left += 1
            right += 1
        return res
