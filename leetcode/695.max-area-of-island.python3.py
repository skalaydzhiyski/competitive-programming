from collections import defaultdict

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        nodes = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    nodes.append( (i,j) )

        def get_neighbours_for(node):
            i, j = node
            res = []
            if 0 <= i + 1 < m and grid[i+1][j]: res.append( (i+1, j) )
            if 0 <= i - 1 < m and grid[i-1][j]: res.append( (i-1, j) )
            if 0 <= j + 1 < n and grid[i][j+1]: res.append( (i, j+1) )
            if 0 <= j - 1 < n and grid[i][j-1]: res.append( (i, j-1) )
            return res

        res = 0
        visited = set()
        for start in nodes:
            current_size = 0
            to_visit = [start]
            while to_visit:
                node = to_visit.pop()
                if node not in visited:
                    current_size += 1
                visited.add(node)
                neighbours = [n for n in get_neighbours_for(node) if n not in visited]
                to_visit += neighbours
            if current_size > res:
                res = current_size
        return res



