class Solution:
  def checkIfExist(self, arr):
    m = {}
    for i,x in enumerate(arr):
      m[x] = set([i]) if x not in m else m[x] | {i}
      
    for i,x in enumerate(arr):
      c = 2*x
      if c not in m:
        continue
      if i not in m[c] or len(m[c] ^ {i}) > 0:
        return True
    return False
    
