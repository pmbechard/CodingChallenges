"""
2839. Check if Strings Can be Made Equal With Operations I
https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/
"""


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        evens_1 = sorted([s1[i] for i in range(len(s1)) if i % 2 == 0])
        evens_2 = sorted([s2[i] for i in range(len(s2)) if i % 2 == 0])

        odds_1 = sorted([s1[i] for i in range(len(s1)) if i % 2 == 1])
        odds_2 = sorted([s2[i] for i in range(len(s2)) if i % 2 == 1])

        return evens_1 == evens_2 and odds_1 == odds_2
