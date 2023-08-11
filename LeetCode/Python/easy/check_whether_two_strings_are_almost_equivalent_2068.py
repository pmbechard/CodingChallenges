"""
2068. Check Whether Two Strings are Almost Equivalent
https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
"""


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for i in set(word1 + word2):
            if abs(word1.count(i) - word2.count(i)) > 3:
                return False
        return True

