"""
1704. Determine if String Halves are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l, r = 0, 0
        s = s.lower()
        mid = (len(s) - 1) // 2
        for i in range(len(s)):
            if s[i] in vowels:
                if i <= mid:
                    l += 1
                else:
                    r += 1
        return l == r
