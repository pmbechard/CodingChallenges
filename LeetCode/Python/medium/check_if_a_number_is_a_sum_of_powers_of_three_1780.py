"""
1780. Check if Number is a Sum of Powers of Three
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        base3 = ''
        while n:
            r = n % 3
            n //= 3
            base3 = f'{r}{base3}'
        return base3.count('2') == 0
