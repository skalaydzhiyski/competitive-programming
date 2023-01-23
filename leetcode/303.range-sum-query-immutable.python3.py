from functools import lru_cache

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    @lru_cache(maxsize=None)
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
