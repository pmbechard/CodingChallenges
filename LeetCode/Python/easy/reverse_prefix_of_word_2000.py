"""
2000. Reverse Prefix of Word
https://leetcode.com/problems/reverse-prefix-of-word
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)
        return word[:idx + 1][::-1] + word[idx + 1:]
