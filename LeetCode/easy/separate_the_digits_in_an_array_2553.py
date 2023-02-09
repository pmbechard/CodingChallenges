"""
2553. Separate the Digits in an Array
https://leetcode.com/problems/separate-the-digits-in-an-array/
"""


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result += [int(i) for i in list(str(num))]
        return result
