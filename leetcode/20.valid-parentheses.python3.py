class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        m = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if len(stack):
                last = stack[-1] 
                if last in '[{(' and m[last] == c:
                    stack.pop()
                    continue
            stack.append(c)
        return len(stack) == 0

