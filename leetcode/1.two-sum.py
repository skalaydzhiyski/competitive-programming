class Solution:
  def twoSum(self, nums, target):
    n = len(nums)

    m = {}
    for i in range(n):
      current = nums[i]
      m[target - current] = i

    for i in range(n):
      current = nums[i]
      if current in m and m[current] != i:
        return [i, m[nums[i]]]


#print(Solution().twoSum([3,2,4], 6))

