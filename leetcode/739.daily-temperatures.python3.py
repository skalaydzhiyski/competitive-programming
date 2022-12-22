from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = deque([0])
        mono = [N-1]
        top = -1
        for idx in range(N-2, -1, -1):
            while len(mono) and temperatures[idx] >= temperatures[mono[top]]:
                _ = mono.pop()
            distance = 0 if len(mono) == 0 else mono[top] - idx
            res.appendleft(distance)
            mono.append(idx)
        return res

