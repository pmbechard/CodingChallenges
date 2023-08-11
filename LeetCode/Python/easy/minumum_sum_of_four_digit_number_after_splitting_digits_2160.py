"""
2160. Minimum Sum of Four Digit Number After Splitting Digits
https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
"""


class Solution:
    def minimumSum(self, num):
        nums = [i for i in str(num)]
        nums.sort()
        num1 = int(nums[0] + nums[3])
        num2 = int(nums[1] + nums[2])
        return num1 + num2
