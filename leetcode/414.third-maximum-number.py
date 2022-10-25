class Solution:
  def thirdMax(self, nums):
    uniq = list(set(nums)) # O(n)
    if len(uniq) in (1,2): return max(uniq)
    fst = max(uniq) # O(len(uniq) <= N)
    snd = max([x for x in uniq if x != fst]) # O(len(uniq) <= N)
    third = max([x for x in uniq if x not in (fst, snd)]) # O(len(uniq) <= N)
    return third
    
