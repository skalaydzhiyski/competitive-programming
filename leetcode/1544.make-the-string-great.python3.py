class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) and abs(ord(c) - ord(res[-1])) == 32:
                res.pop()
                continue
            res.append(c)
        return ''.join(res)
