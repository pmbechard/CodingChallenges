"""
3330. Find the Original Typed String I
https://leetcode.com/problems/find-the-original-typed-string-i/
"""


class Solution:
    def possibleStringCount(self, word: str) -> int:
        dups = 0
        prev = word[0]
        for c in word:
            if c == prev:
                dups += 1
            prev = c
        return dups
