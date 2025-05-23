"""
1869. Longer Contiguous Segments of Ones than Zeros
https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = max_ones = twos = max_twos = 0
        for c in s:
            if c == '1':
                twos = 0
                ones += 1
                max_ones = max(max_ones, ones)
            else:
                ones = 0
                twos += 1
                max_twos = max(max_twos, twos)
        return max_ones > max_twos
