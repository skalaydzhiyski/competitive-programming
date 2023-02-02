class Solution:
    def greatestLetter(self, s: str) -> str:
        lowers, uppers = set(), set()
        for c in s:
            if c.isupper():
                uppers.add(c)
            else:
                lowers.add(c)
        res = ""
        for c in uppers:
            if c.lower() in lowers and c > res:
                res = c
        return res 


