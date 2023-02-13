"""
2562. Find the Array Concatenation Value
https://leetcode.com/problems/find-the-array-concatenation-value/
"""


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        while nums:
            if len(nums) == 1:
                return result + nums[0]
            result += int(str(nums[0]) + str(nums[-1]))
            nums = nums[1:-1]
        return result
