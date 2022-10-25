class Solution:
  def heightChecker(self, heights):
    # build counts
    m = {}
    for h in heights: # O(n) < 100
      m[h] = 1 if h not in m else m[h] + 1
    
    # build expected
    expected = []
    for k in range(1, max(heights) + 1): # O(max(heights)) < 100
      if k not in m: continue
      expected += [k for _ in range(m[k])]  
      
    # get num diffs
    res = sum([x != y for x,y in zip(heights, expected)])
    return res
    
