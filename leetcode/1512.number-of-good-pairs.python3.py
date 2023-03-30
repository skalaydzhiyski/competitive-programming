class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(N):
                if i < j and nums[i] == nums[j]:
                    res += 1
        return res
