from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = Counter(nums)
        return sum([n for n, count in m.items() if count == 1])
