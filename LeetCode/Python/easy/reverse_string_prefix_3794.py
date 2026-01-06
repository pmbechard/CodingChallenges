"""
3794. Reverse String Prefix
https://leetcode.com/problems/reverse-string-prefix/
"""


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]
