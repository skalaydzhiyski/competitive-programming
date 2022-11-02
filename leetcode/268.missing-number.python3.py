# Gauss formula for summation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = (n*(n+1))//2
        return expected - sum(nums)

# Bit manipulation
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)+1): res ^= i
        for x in nums: res ^= x
        return res


# Mark every seen number with a string (because we have a 0 we cannot perform the trick with flipping the sign.)
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nums.append(1)
        for i in range(N):
            current = nums[i] if type(nums[i]) == int else int(nums[i])
            nums[current] = str(nums[current])
        return [i for i,x in enumerate(nums) if type(x) == int][0]