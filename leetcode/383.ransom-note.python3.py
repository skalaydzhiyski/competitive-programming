class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        storern, storemag = defaultdict(int), defaultdict(int)
        for c in ransomNote: storern[c] += 1
        for c in magazine: storemag[c] += 1

        for c,v in storern.items():
            if c not in storemag or storern[c] > storemag[c]:
                return False
        return True
