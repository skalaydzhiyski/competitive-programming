from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)
        for x in nums:
            m[x] += 1
        for key, value in m.items():
            if value > n / 2:
                return key
        return 0