class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nums.append(1)
        for i in range(N):
            current = nums[i] if type(nums[i]) == int else int(nums[i])
            nums[current] = str(nums[current])
        return [i for i,x in enumerate(nums) if type(x) == int][0]