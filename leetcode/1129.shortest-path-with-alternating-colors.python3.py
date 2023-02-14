from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        red, blue = defaultdict(list), defaultdict(list)
        for start, end in redEdges:
            red[start].append(end)
        for start, end in blueEdges:
            blue[start].append(end)

        res = [-1 for _ in range(n)]
        for first, second in [(red, blue), (blue, red)]:
            visited = set()
            to_visit = deque([ ((0,False), 0) ])
            while to_visit:
                (current, flag), distance = to_visit.popleft()

                if res[current] == -1 or distance < res[current]:
                    res[current] = distance

                next_flag = not flag
                next_ = first[current] if next_flag else second[current]
                for node in next_:
                    next_state = (node, next_flag)
                    if next_state not in visited:
                        visited.add(next_state)
                        to_visit.append((next_state, distance + 1))
        return res
