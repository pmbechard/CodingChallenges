"""
561. Array Partition I
https://leetcode.com/problems/array-partition-i/
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums_copy = nums[:]
        nums_copy.sort()
        result = [nums_copy[x] for x in range(0, len(nums_copy), 2)]
        return sum(result)