class Solution:
  def findMaxConsecutiveOnes(self, nums):
    N = len(nums)
    nz = 0
    zi = -1
    current = 0
    res = -1
    for i in range(N):
      if nums[i] == 1:
        current += 1
      else:
        if nz == 0:
          current += 1
          nz = 1
          zi = i
        else:
          current = i - zi
          zi = i
      if current > res:
        res = current
    return res

