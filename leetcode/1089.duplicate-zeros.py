class Solution:
  def duplicateZeros(self, arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    N = len(arr)
    res = []
    l = 0
    i = 0
    while l < N:
      if arr[i] != 0:
        res += [arr[i]]
        l += 1
      else:
        res += [0, 0]
        l += 2
      i += 1
    for i in range(N):
      arr[i] = res[i]



arr = [1,0,2,3,0,4,5,0]
res = Solution().duplicateZeros(arr)
print(res)

arr = [1,0,2,3]
res = Solution().duplicateZeros(arr)
print(res)
