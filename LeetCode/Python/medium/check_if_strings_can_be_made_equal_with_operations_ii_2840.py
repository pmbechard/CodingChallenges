"""
2840. Check if Strings Can be Made Equal With Operations II
https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
"""


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) < 3:
            return s1 == s2
        s1_evens, s2_evens = [], []
        for i in range(0, len(s1), 2):
            s1_evens.append(s1[i])
            s2_evens.append(s2[i])
        if sorted(s1_evens) != sorted(s2_evens):
            return False
        s1_odds, s2_odds = [], []
        for i in range(1, len(s1), 2):
            s1_odds.append(s1[i])
            s2_odds.append(s2[i])
        if sorted(s1_odds) != sorted(s2_odds):
            return False
        return True
