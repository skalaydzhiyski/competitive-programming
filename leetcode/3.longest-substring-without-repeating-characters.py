class Solution:
  def lengthOfLongestSubstring(self, s):
    n = len(s)
    if n == 0: return 0
    res, count = 1,1
    i, j = 0, 1
    m = {}
    m[s[i]] = 1
    while j<n:
      if s[j] not in m: 
        m[s[j]] = 1
        count += 1
        j += 1
      else:
        i += 1
        j = i+1
        count = 1
        m = {s[i]:1}
      res = max(res, count)
    return res
