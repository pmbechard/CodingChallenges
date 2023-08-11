"""
520. Detect Capital
https://leetcode.com/problems/detect-capital/
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
