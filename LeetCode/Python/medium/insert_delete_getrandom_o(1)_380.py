"""
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1
"""


class RandomizedSet:

    def __init__(self):
        self.arr = set()

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        self.arr.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.arr))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
