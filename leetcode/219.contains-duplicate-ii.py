class Solution:
  def containsNearbyDuplicate(self, nums, k):
    m = {}
    n = len(nums)
    for i in range(n):
      if nums[i] not in m:
        m[nums[i]] = i
      else:
        print(m[nums[i]], i, k)
        if abs(m[nums[i]] - i) <= k:
          return True
        else:
          m[nums[i]] = i
    return False
