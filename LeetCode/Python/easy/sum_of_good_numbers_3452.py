"""
3452. Sum of Good Numbers
https://leetcode.com/problems/sum-of-good-numbers/
"""


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        output = 0
        for i in range(len(nums)):
            l = r = False
            if i - k < 0 or nums[i - k] < nums[i]:
                l = True
            if i + k > len(nums) - 1 or nums[i + k] < nums[i]:
                r = True
            if l and r:
                output += nums[i]
        return output