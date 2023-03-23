from collections import defaultdict, deque

class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        m = [0] * (n+1)
        for q in queries:
            m[q] += 1
        res = m[1] % 2
        for idx in range(2, n+1):
            m[idx] += m[idx//2] # update with parent's value (latest value because we iterate DOWN the tree)
            res += m[idx] % 2
        return res

