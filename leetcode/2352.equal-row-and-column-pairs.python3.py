class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        rows, cols = defaultdict(int), defaultdict(int)
        for row in grid: rows[tuple(row)] += 1

        for j in range(len(grid)):
            col = [r[j] for r in grid]
            cols[tuple(col)] += 1

        res = 0
        for r in rows:
            if r not in cols: continue
            res += rows[r] * cols[r]
        return res
