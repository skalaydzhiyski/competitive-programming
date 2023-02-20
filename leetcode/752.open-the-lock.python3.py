from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        chars = '0123456789'
        directions = [(0,1),(0,-1),(1,1),(1,-1),(2,1),(2,-1),(3,1),(3,-1)]
        visited = set()
        start = '0000'
        if start in deadends:
            return -1

        to_visit = deque([ (start, 0) ])
        while to_visit:
            current, distance = to_visit.popleft()
            if current == target:
                return distance
            for idx, direction in directions:
                next_ = list(current)
                next_[idx] = chars[ (int(next_[idx]) + direction) % 10 ]
                next_ = ''.join(next_)
                if next_ not in deadends and next_ not in visited:
                    visited.add(next_)
                    to_visit.append((next_, distance + 1))
        return -1
