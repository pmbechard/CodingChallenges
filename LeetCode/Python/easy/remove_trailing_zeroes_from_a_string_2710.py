"""
2710. Remove Trailing Zeros From a String
https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
"""


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return str(int(num[::-1]))[::-1]
