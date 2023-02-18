from collections import deque
from copy import deepcopy
import math

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        in_bounds = lambda x,y: 0 <= x < m and 0 <= y < n
        houses = set()
        total = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    houses.add((i,j))

        visited_marker = 0
        for house in houses:
            res = math.inf
            to_visit = deque([ (house, 0) ])
            while to_visit:
                (x,y), distance = to_visit.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if in_bounds(nx, ny) and grid[nx][ny] == visited_marker:
                        total[nx][ny] += distance + 1
                        res = min(res, total[nx][ny])
                        grid[nx][ny] -= 1
                        to_visit.append( ((nx, ny), distance + 1) )

            visited_marker -= 1
            if res == math.inf:
                return -1
        return res