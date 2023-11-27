"""
935. Knight Dialer
https://leetcode.com/problems/knight-dialer/
"""


class Solution:
    num_map = {
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
        0: [4, 6]
    }
    mem = dict()

    def knightDialer(self, n: int) -> int:
        output = 0
        for num in self.num_map:
            output += self.traverse(num, n, n)
        return output % (10 ** 9 + 7)

    def traverse(self, node, count, target):
        if count == 1:
            return 1
        elif self.mem.get((node, count)) != None:
            return self.mem[(node, count)]
        output = 0
        for val in self.num_map[node]:
            output += self.traverse(val, count - 1, target)
        self.mem[(node, count)] = output
        return output
