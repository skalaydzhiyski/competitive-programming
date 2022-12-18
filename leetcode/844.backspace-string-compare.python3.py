class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parse(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                    continue
                if len(stack) != 0:
                    stack.pop()
            return ''.join(stack)
        return parse(s) == parse(t)

