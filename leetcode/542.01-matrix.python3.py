from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def get_neighbours_for(node):
            i,j = node
            directions = (1,0), (-1,0), (0,1), (0,-1)
            neighbours = [(i+di, j+dj) for di,dj in directions]
            return [
                (x,y)
                for x,y in neighbours
                if 0 <= x < m and 0 <= y < n
            ]

        res = mat.copy()
        ones = set()
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    ones.add((i,j))
                    res[i][j] = None

        visited = set()
        for one in ones:
            if one in visited:
                continue

            to_visit = deque([one])
            while to_visit:
                node = to_visit.popleft()
                visited.add(node)
                neighbours = get_neighbours_for(node)

                if any([mat[x][y] == 0 for x,y in neighbours]):
                    res[node[0]][node[1]] = 1
                    continue

                seen = []
                for x,y in neighbours:
                    if res[x][y]:
                        seen.append(mat[x][y])
                if len(seen):
                    res[node[0]][node[1]] = min(seen) + 1
                    continue

                to_visit += [n for n in neighbours if n not in visited]
                to_visit.append(node)
                
        return res
