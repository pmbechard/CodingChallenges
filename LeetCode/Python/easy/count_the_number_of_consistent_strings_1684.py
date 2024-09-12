"""
1684. Count the Number of Consistent Strings
https://leetcode.com/problems/count-the-number-of-consistent-strings/
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ctr = 0
        for s in words:
            if not set(s).difference(allowed):
                ctr += 1
        return ctr
