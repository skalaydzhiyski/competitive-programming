class Solution:
  def searchInsert(self, nums, target):
    left,right = 0,len(nums)-1
    while left <= right:
      m = (left + right) // 2
      print(left, right, m, nums[left:right+1], nums[m])
      if nums[m] == target:
        return m
      elif target > nums[m]:
        left = m+1
      elif target < nums[m]:
        right = m-1
    print(left, right)
    return left
