"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if not t and s: return False
        if not s: return True
        s_i = 0
        for letter in t:
            if letter == s[s_i]:
                s_i += 1
                if s_i == len(s):
                    return True
        return False
