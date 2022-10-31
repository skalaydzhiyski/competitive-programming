from multiprocessing import Queue
class Solution:
    def longestOnes(self, nums, k):
        N = len(nums)
        zeros = Queue()
        for i in range(N):
            if nums[i] == 0: zeros.put(i)

        res, current = 0, 0
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


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
res = Solution().longestOnes(nums, k)
print(res)