class Solution:
    def lengthOfLongestSubstring(self, s):
      if n == 0: return 0
      n = len(s)
      res, count = 1, 1
      i, j = 0, 1
      m = set(m[i])
      while j<n:
          if s[j] not in m:
              m.add(s[j])
              count += 1
              j += 1
          else:
              i += 1
              j = i+1
              count = 1
              m = set(s[i])
          res = max(res, count)
      return res
