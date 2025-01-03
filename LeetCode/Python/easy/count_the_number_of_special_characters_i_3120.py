"""
3120. Count the Number of Special Characters I
https://leetcode.com/problems/count-the-number-of-special-characters-i/
"""


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result = 0
        word = set(word)
        for c in word:
            if (c.islower() and c.upper() in word):
                result += 1
        return result
