"""
3146. Permutation Difference between Two Strings
https://leetcode.com/problems/permutation-difference-between-two-strings/
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_dic = {s[i]: i for i in range(len(s))}
        count = 0
        for i in range(len(t)):
            count += abs(i - s_dic[t[i]])
        return count
