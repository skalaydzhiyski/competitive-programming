from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        q = deque()
        res = []
        for current in range(N):
            # maintain monotonic decreasing property
            while q and nums[current] >= nums[q[-1]]:
                _ = q.pop()
            q.append(current)
            # if the current max is off window -> remove
            if q[0] + k <= current:
                q.popleft()
            # accumulate result list
            if current >= k-1:
                res.append(nums[q[0]])
        return res
