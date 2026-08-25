class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_element = val
        if len(self.stack) > 0:
            min_element = val if val < self.stack[-1][1] else self.stack[-1][1]
        self.stack.append([val,min_element]) 

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
