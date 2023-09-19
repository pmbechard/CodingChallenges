"""
1925. Count Square Sum Triples
https://leetcode.com/problems/count-square-sum-triples/
"""


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n):
            for b in range(a + 1, n):
                c = sqrt(a ** 2 + b ** 2)
                if 1 <= c <= n and c == int(c):
                    count += 2
        return count
