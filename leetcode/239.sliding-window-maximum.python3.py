from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        q = deque()
        res = []
        for idx in range(N):
            while q and nums[idx] > nums[q[-1]]:
                q.pop()

            q.append(idx)
            
            if q[0] + k == idx:
                q.popleft()

            if idx >= k-1:
                res.append(nums[q[0]])
        return res



