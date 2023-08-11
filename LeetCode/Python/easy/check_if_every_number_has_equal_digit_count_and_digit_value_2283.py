"""
2283. Check if Number Has Equal Digit Count and Digit Value
https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
"""


class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if str(num.count(str(i))) != num[i]:
                return False
        return True
