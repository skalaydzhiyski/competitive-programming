class Solution:
  def replaceElements(self, arr):
    N = len(arr)
    m = -1
    for i in range(N-1, -1, -1):
      c = arr[i]
      arr[i] = m
      if c > m: m = c
    return arr
