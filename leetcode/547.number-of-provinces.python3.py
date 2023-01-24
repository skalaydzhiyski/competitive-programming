from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [0] * N
        m = {node: [] for node in range(N)}
        for i in range(N):
            for j in range(i+1, N):
                if isConnected[i][j]:
                    m[i].append(j)
                    m[j].append(i)
        res = 0
        for node in range(N):
            if visited[node]: continue
            to_visit = [node]
            while to_visit:
                current = to_visit.pop()
                visited[current] = 1
                to_visit += [x for x in m[current] if not visited[x]]
            res += 1
        return res
