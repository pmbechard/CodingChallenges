"""
3856. Trim Trailing Vowels
https://leetcode.com/problems/trim-trailing-vowels/
"""


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        while s and s[-1] in 'aeiou':
            s = s[:-1]
        return s
