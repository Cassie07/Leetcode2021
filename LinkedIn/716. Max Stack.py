class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            m = x
        else:
            m = max(x, self.stack[-1][1])
        self.stack.append((x,m))
        

    def pop(self) -> int:
        res = self.stack.pop()
        return res[0]

    def top(self) -> int:
        res = self.stack.pop()
        self.stack.append(res)
        return res[0]

    def peekMax(self) -> int:
        res = self.stack.pop()
        self.stack.append(res)
        return res[1]
        

    def popMax(self) -> int:
        count = 0
        memo = []
        m = self.stack[-1][1]
        while self.stack[-1][0] != m:
            tmp = self.stack.pop()
            memo.append(tmp)
        res = self.stack.pop()716. Max Stack
