"""
1945. Sum of Digits of String After Convert
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = int(''.join([str(ord(i)-96) for i in s]))
        for i in range(k):
            total = sum([int(i) for i in str(total)])
        return total
