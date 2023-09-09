"""
1974. Minimum Time to Type Word Using Special Typewriter
https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        location = 97
        result = len(word)
        for char in word:
            result += min(abs(location - ord(char)), 26 - abs(location - ord(char)))
            location = ord(char)
        return result
