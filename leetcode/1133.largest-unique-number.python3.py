class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        store = defaultdict(int)
        for x in nums: store[x] += 1
        store = [k for k,v in store.items() if v == 1]
        return -1 if not len(store) else max(store)