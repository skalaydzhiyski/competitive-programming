class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from collections import defaultdict
        dsum = lambda x: sum([int(d) for d in str(x)])
        store = defaultdict(int)
        res = -1
        for x in nums:
            s = dsum(x)
            if s in store:
                res = max(res, store[s] + x)
            store[s] = max(store[s], x)
        return res
