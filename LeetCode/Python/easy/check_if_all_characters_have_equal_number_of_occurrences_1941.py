"""
1941. Check if All Characters Have Equal Number of Occurrences
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
"""


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurrences = s.count(s[0])
        letters = set(s)
        for i in letters:
            if s.count(i) != occurrences:
                return False
        return True
