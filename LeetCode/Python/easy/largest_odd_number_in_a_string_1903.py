"""
1903. Largest Odd Number in String
https://leetcode.com/problems/largest-odd-number-in-string/
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_odd = -1
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                last_odd = i
                break
        return num[:last_odd + 1]
