"""
2315. Count Asterisks
https://leetcode.com/problems/count-asterisks/
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        while '|' in s:
            l = s.find('|')
            r = s.find('|', l+1)
            s = s[:l] + s[r+1:]
        return s.count('*')
