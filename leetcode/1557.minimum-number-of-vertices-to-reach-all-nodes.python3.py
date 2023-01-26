class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes_with_parents = set([right for _, right in edges])
        return [
            node
            for node in range(n)
            if node not in nodes_with_parents
        ]
