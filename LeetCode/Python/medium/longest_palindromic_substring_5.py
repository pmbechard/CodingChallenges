"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        result = ""
        for i in range(len(s)):
            if i > 0 and s[i - 1] == s[i]:
                palindrome = self.check_palidromes(s, i - 1, i)
                if len(palindrome) > len(result):
                    result = palindrome
            palindrome = self.check_palidromes(s, i, i)
            if len(palindrome) > len(result):
                result = palindrome
        return result

    def check_palidromes(self, s, left, right):
        while True:
            if left > 0 and right < len(s) - 1:
                if s[left - 1] == s[right + 1]:
                    return self.check_palidromes(s, left - 1, right + 1)
            return s[left:right + 1]
