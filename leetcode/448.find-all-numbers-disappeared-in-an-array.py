class Solution:
  def findDisappearedNumbers(self, nums):
    for n in nums:
      idx = abs(n) - 1
      if nums[idx] > 0:
        nums[idx] = -1 * nums[idx]
    return [i+1 for i,x in enumerate(nums) if x > 0]

