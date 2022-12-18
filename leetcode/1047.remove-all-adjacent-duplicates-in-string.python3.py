class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) == 0 or c != res[-1]:
                res.append(c)
                continue
            res.pop()
        return ''.join(res)
