from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m, rev = {}, {}
        for left, right in zip(s, t):
            if right not in m:
                m[right] = left
            if left not in rev:
                rev[left] = right
        
            if m[right] != left or rev[left] != right:
                return False
        return True