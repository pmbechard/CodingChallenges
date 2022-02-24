"""
2108. Find First Palindromic String in the Array
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
"""


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindromic(word):
                return word
        return ""

    def is_palindromic(self, word):
        counter = 0
        for i in range(len(word) // 2):
            if not word[0 + i] == word[-1 - i]:
                return False
        return True
