"""
1704. Determine if String Halves are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        l, r = 0, 0
        for vowel in vowels:
            l += s.lower().count(vowel, 0, len(s)//2)
            r += s.lower().count(vowel, len(s)//2)
        return r == l
