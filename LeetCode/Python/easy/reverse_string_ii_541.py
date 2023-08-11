"""
541. Reverse String II
https://leetcode.com/problems/reverse-string-ii/
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for i in range(0, len(s), k * 2):
            s = s[:i] + s[i:i + k][::-1] + s[i + k:]
        return s
