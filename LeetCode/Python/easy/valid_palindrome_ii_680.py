"""
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        elif len(s) == 2:
            return True
        elif len(s) == 3:
            return s[0] == s[1] or s[0] == s[2] or s[1] == s[2]
        elif s == s[::-1]:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.is_palindrome(s[l + 1:r + 1]) or self.is_palindrome(s[l:r])
            l += 1
            r -= 1
        return True

    def is_palindrome(self, s):
        return s == s[::-1]
