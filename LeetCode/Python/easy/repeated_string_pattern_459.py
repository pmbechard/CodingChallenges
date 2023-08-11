"""
459. Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if not s.replace(s[:i + 1], ''):
                return True
        return False
