class Solution:
  def merge(self, nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    res = []
    i,j = 0,0
    while i < m or j < n:
      if i < m and j >= n:
        res.append(nums1[i])
        i += 1
        continue
      if i >= m and j < n:
        res.append(nums2[j])
        j += 1
        continue
      if nums1[i] <= nums2[j]:
        res.append(nums1[i])
        i += 1
      else:
        res.append(nums2[j])
        j += 1
    for i in range(m+n): nums1[i] = res[i]
