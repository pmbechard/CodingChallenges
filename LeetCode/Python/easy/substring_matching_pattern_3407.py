"""
3407. Substring Matching Pattern
https://leetcode.com/problems/substring-matching-pattern/
"""


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p1, p2 = p.split('*')
        p1i = s.find(p1)
        if p1i == -1:
            return False
        if p2 in s[p1i + len(p1):]:
            return True
        return False
