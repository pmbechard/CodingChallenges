"""
2396. Strictly Palindromic Number
https://leetcode.com/problems/strictly-palindromic-number
"""

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            if not self.check_palindrome(self.change_base(n, i)):
                return False
        return True

    def change_base(self, n: int, b: int) -> str:
        div = n // b
        remainder = n % b
        if n == 0:
            return '0'
        elif div == 0:
            return str(remainder)
        else:
            return self.change_base(div, b) + str(remainder)

    def check_palindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
