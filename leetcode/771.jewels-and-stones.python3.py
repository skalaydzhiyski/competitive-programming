class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        store = set(jewels)
        return sum([x in store for x in stones])        
