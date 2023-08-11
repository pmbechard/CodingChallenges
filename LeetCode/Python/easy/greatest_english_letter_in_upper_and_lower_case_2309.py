"""
2309. Greatest English Letter in Upper and Lower Case
https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        options = [i for i in s if i.isupper() and i.lower() in s]
        length = len(options)
        if length == 0:
            return ''
        elif length == 1:
            return options[0]
        else:
            return sorted(options)[-1]
