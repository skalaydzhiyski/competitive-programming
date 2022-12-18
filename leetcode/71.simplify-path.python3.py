class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        parts = [p for p in path.split('/') if len(p)]
        for part in parts:
            if part == '.':
                continue
            if part == '..':
                if len(res): res.pop()
                continue
            res.append(part)
        return '/' + '/'.join(res)

        
