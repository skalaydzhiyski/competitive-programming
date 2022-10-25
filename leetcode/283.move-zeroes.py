class Solution:
  def moveZeroes(self, nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    N = len(nums)
    for i in range(N-1):
      if nums[i] != 0:
        continue
      j = i + 1
      while j < N and nums[j] == 0:
        j += 1
      if j == N:
        break
      temp = nums[i]
      nums[i] = nums[j]
      nums[j] = temp

