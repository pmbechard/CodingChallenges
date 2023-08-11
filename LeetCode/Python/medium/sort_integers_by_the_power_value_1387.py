"""
1387. Sort Integers by The Power Value
https://leetcode.com/problems/sort-integers-by-the-power-value/
"""


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        results = []
        for i in range(lo, hi + 1):
            orig = i
            count = 0
            while i != 1:
                if i % 2 == 0:
                    i /= 2
                else:
                    i = 3 * i + 1
                count += 1
            results.append([orig, count])
        results.sort(key=lambda x: x[1])
        return results[k - 1][0]
