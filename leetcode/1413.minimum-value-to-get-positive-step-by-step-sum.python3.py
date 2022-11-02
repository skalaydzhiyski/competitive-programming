class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minpref = 2**31
        running = 0
        for i in range(len(nums)):
            running = nums[i] if i == 0 else nums[i] + running
            if running < minpref:
                minpref = running
        return 1 if minpref > 0 else abs(minpref) + 1
            

