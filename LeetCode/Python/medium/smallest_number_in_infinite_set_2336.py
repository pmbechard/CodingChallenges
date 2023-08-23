"""
2336. Smallest Number in Infinite Set
https://leetcode.com/problems/smallest-number-in-infinite-set/
"""


class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.removed = []

    def popSmallest(self) -> int:
        num = self.current
        self.removed.append(num)
        self.current += 1
        while self.current in self.removed:
            self.current += 1
        return num

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
        if num < self.current:
            self.current = num

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
