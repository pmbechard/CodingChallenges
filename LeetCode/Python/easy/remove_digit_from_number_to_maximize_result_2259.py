"""
2259. Remove Digit From Number to Maximize Result
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = 0
        for i in range(len(number)):
            if number[i] == digit and int(number[:i] + number[i + 1:]) > int(max_num):
                max_num = number[:i] + number[i + 1:]
        return max_num
