from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        target = 0
        visited = set()
        to_visit = deque([ start ])
        while to_visit:
            current = to_visit.popleft()
            if arr[current] == target:
                return True
            for i in (current - arr[current], current + arr[current]):
                if 0 <= i < n and i not in visited:
                    visited.add(i)
                    to_visit.append(i)
        return False