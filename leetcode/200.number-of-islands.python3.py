class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def get_neighbours_for(position):
            i, j = position
            res = []
            if i-1 >= 0: res.append((i-1, j))
            if i+1 < m: res.append((i+1, j))
            if j-1 >= 0: res.append((i, j-1))
            if j+1 < n: res.append((i, j+1))
            res = [(i,j) for i,j in res if not visited[i][j] and grid[i][j] != "0"]
            return res

        def dfs(node):
            x,y = node
            visited[x][y] = 1
            to_visit = get_neighbours_for(node)
            while to_visit:
                current = to_visit.pop()
                visited[current[0]][current[1]] = 1
                next_ = get_neighbours_for(current)
                to_visit += next_

        res = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                res += 1
                node = (i,j)
                dfs(node)
        return res
