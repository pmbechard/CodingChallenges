"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x):
        if -(2 ** 31) <= x <= 2 ** 31 - 1:
            x_list = [i for i in str(x)]
            rev = list(reversed(x_list))
            return True if x_list == rev else False
