class Solution:
  def removeDuplicates(self, nums):
    N = len(nums)
    if N == 1: return 1
    res = 1
    prev_k = 1
    for i in range(N-1):
      j = i+1
      if nums[i] >= nums[j]:
        k = prev_k
        while k < N and nums[i] >= nums[k]:
          k += 1
        if k == N: break
        prev_k = k
        nums[j] = nums[k]
      res += 1
    return res
