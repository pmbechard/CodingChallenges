"""
2544. Alternating Digit Sum
https://leetcode.com/problems/alternating-digit-sum/
"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        n = str(n)
        for i in range(len(n)):
            if i % 2 == 0:
                result += int(n[i])
            else:
                result -= int(n[i])
        return result
