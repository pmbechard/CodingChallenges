"""
2670. Find the Distinct Difference Array
https://leetcode.com/problems/find-the-distinct-difference-array/
"""


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(len(set(nums[:i + 1])) - len(set(nums[i + 1:])))
        return result
