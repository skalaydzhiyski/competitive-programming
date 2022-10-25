class Solution:
  def sortArrayByParity(self, nums):
    N = len(nums)
    is_even = lambda x: x % 2 == 0
    for i in range(N-1):
      if is_even(nums[i]):
        continue
      j = i+1
      while j < N and not is_even(nums[j]):
        j += 1
      if j == N:
        break
      temp = nums[i]
      nums[i] = nums[j]
      nums[j] = temp
    return nums
