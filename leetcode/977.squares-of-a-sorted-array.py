class Solution:
  def sortedSquares(self, nums):
    if len(nums) == 0:
      return []
    elif len(nums) == 1:
      return [nums[0]**2]

    if nums[0] >= 0:
      return [x**2 for x in nums]
    if nums[-1] < 0:
      nums.reverse()
      return [x**2 for x in nums]

    N = len(nums)
    right = [idx for idx in range(N) if nums[idx] >= 0][0]
    nums = [x**2 for x in nums]
    left = right - 1 if right > 0 else 0
    res = []
    while True:
      if left >= 0 and right < N:
        if nums[left] <= nums[right]:
          res.append(nums[left])
          left -= 1
        else:
          res.append(nums[right])
          right += 1
      elif left < 0 and right < N:
        res.append(nums[right])
        right += 1
      elif left >= 0 and right >= N:
        res.append(nums[left])
        left -= 1
      else:
        break
    return res

