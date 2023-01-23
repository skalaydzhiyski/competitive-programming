from collections import deque

class MinStack:
    def __init__(self):
        self.q = deque()
        self.side = []

    def push(self, val: int) -> None:
        if not self.q:
            self.q.append(val)
            self.side.append('top')
        else:
            if val < self.q[0]:
                self.q.appendleft(val)
                self.side.append('bottom')
            else:
                self.q.append(val)
                self.side.append('top')


    def pop(self) -> None:
        side = self.side.pop()
        if side == 'top':
            self.q.pop()
        else:
            self.q.popleft()

    def top(self) -> int:
        if self.side[-1] == 'top':
            return self.q[-1]
        return self.q[0]

    def getMin(self) -> int:
        return self.q[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
