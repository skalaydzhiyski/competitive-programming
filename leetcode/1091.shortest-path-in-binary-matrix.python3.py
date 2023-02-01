from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        def get_neighbours_for(node):
            i, j = node
            return [
                (i+1,j), (i-1,j),
                (i,j+1), (i,j-1),
                (i+1, j+1), (i+1,j-1),
                (i-1,j-1), (i-1,j+1)
            ]

        target = (N-1, N-1)
        res = []

        grid[0][0] = 1
        frame = (0,0)
        distance = 1
        to_visit = deque([frame])
        while to_visit:
            node = to_visit.popleft()
            distance = grid[node[0]][node[1]]
            if node == target:
                return distance
            neighbours = [
                n for n in get_neighbours_for(node)
                if 0 <= n[0] < N
                and 0 <= n[1] < N
                and grid[n[0]][n[1]] == 0
            ]
            for n in neighbours:
                grid[n[0]][n[1]] = distance + 1
                to_visit.append(n)

        return -1 if len(res) == 0 else min(res)
