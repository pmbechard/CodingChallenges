"""
2496. Maximum Value of a String in an Array
https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
"""


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max = 0
        for num in strs:
            if num.isnumeric():
                current = int(num)
            else:
                current = len(num)
            if current > max:
                max = current
        return max
