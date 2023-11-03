"""
2903. Find Indices With Index and Value Difference I
https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/
"""


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums) - indexDifference):
            for j in range(i + indexDifference, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
