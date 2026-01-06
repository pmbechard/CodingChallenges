"""
3745. Maximize Expression of Three Elements
https://leetcode.com/problems/maximize-expression-of-three-elements/
"""


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] + nums[-2] - nums[0]
