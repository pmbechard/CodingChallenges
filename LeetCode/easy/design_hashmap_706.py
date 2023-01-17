"""
706. Design HashMap
https://leetcode.com/problems/design-hashmap/description/
"""


class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        for i in self.map:
            if i[0] == key:
                i[1] = value
                return
        self.map.append([key, value])

    def get(self, key: int) -> int:
        for i in self.map:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        index = -1
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                index = i
                break
        if index != -1:
            self.map = self.map[:index] + self.map[index + 1:]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
