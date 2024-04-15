"""
1417. Reformat The String
https://leetcode.com/problems/reformat-the-string
"""


class Solution:
    def reformat(self, s: str) -> str:
        alpha, numer = [], []
        for c in s:
            if c.isnumeric():
                numer.append(c)
            else:
                alpha.append(c)
        if abs(len(alpha) - len(numer)) > 1:
            return ''
        result = [None] * (len(s))
        try:
            result[::2], result[1::2] = alpha, numer
        except:
            result[::2], result[1::2] = numer, alpha
        return ''.join(result)
