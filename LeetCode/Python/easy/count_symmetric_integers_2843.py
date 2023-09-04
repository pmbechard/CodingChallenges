"""
2843. Count Symmetric Integers
https://leetcode.com/problems/count-symmetric-integers/
"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            i = str(i)
            if len(i) % 2 != 0:
                continue
            l = sum([int(x) for x in i[:len(i) // 2]])
            r = sum([int(x) for x in i[len(i) // 2:]])
            if r == l:
                count += 1
        return count
