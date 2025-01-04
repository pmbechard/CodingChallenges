"""
3136. Valid Word
https://leetcode.com/problems/valid-word/
"""


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vow = cons = False
        for c in word:
            if not c.isalnum():
                return False
            if c.lower() in vowels:
                vow = True
            if c.isalpha() and c.lower() not in vowels:
                cons = True
        return vow and cons
