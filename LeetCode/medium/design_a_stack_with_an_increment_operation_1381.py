"""
1381. Design a Stack With Increment Operation
https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))
        for i in range(k):
            self.stack[i] += val
