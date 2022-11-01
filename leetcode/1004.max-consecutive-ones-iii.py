# SLIDING WINDOW SOLUTION (O(N) time; O(1) space)
class Solution:
    def longestOnes(self, nums, k):
        N = len(nums)
        left = 0
        current = res = 0
        for right in range(N):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1

# QUEUE SOLUTION (O(N) time; O(N) space)
from multiprocessing import Queue
class Solution2:
    def longestOnes(self, nums, k):
        N = len(nums)
        zeros = Queue()
        for i in range(N):
            if nums[i] == 0: zeros.put(i)
        current = res = 0
        for i in range(N):
            if nums[i] == 1:
                current += 1
            else:
                if k > 0:
                    current += 1
                    k -= 1
                else:
                    current = i - zeros.get()
            if current > res:
                res = current
        return res


nums = [1,0,0,1,1,0,1]
k = 1
res = Solution2().longestOnes(nums, k)
print(res)