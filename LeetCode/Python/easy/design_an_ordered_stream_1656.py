"""
1656. Design an Ordered Stream
https://leetcode.com/problems/design-an-ordered-stream/
"""


class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.stream[idKey] = value
        if idKey == self.pointer:
            while self.pointer < len(self.stream) and self.stream[self.pointer]:
                self.pointer += 1
            return self.stream[idKey:self.pointer]
        return None

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
