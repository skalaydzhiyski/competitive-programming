class Solution:
  def removeElement(self, nums, val):
    res = []
    k = 0
    for n in nums:
      if n != val:
        res.append(n)
        k += 1
    for i in range(k):
      nums[i] = res[i]
    return k
