from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for x in nums:
            m[x] += 1
        res = [k for k,v in m.items() if v == 1][0]
        return res