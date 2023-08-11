"""
155. Min Stack
https://leetcode.com/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack = self.stack[:-1]

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)
