"""
2578. Split With Minimum Sum
https://leetcode.com/problems/split-with-minimum-sum/
"""


class Solution:
    def splitNum(self, num: int) -> int:
        nums = sorted([int(x) for x in str(num)])
        num1 = num2 = ''
        for i in range(len(nums)):
            if i % 2 == 0:
                num1 += str(nums[i])
            else:
                num2 += str(nums[i])
        return int(num1) + int(num2)
