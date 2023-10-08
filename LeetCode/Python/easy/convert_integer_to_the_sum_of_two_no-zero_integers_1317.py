"""
1317. Convert Integer to the Sum of Two No-Zero Integers
https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
"""


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n - 1
        while a > 0:
            if '0' not in str(a) + str(n - a):
                return [n - a, a]
            a -= 1
