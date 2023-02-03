# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        stack = [root]
        while stack:
            current = stack.pop()
            if current.left:
                stack.append(current.left)
                graph[current.val].append(current.left.val)
                graph[current.left.val].append(current.val)
            if current.right:
                stack.append(current.right)
                graph[current.val].append(current.right.val)
                graph[current.right.val].append(current.val)
        res = []
        visited = set()
        frame = (target.val, 0)
        to_visit = deque([frame])
        while to_visit:
            current, level = to_visit.popleft()
            visited.add(current)
            if level == k:
                res.append(current)
            if level > k:
                break
            to_visit += [(n, level + 1) for n in graph[current] if n not in visited]
        return res

