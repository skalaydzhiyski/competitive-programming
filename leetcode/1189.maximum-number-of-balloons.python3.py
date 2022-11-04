class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import defaultdict
        store = defaultdict(int)
        for c in text: store[c] += 1
        for c in 'lo': store[c] //= 2
        return min([store[c] for c in 'balon'])