"""
917. Reverse Only Letters
https://leetcode.com/problems/reverse-only-letters/
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalpha():
                l += 1
                continue
            if not s[r].isalpha():
                r -= 1
                continue
            s = s[:l] + s[r] + s[l + 1:r] + s[l] + s[r + 1:]
            l += 1
            r -= 1
        return s
