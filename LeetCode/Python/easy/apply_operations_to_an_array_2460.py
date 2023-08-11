"""
2460. Apply Operations to an Array
https://leetcode.com/problems/apply-operations-to-an-array/
"""


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                continue
            elif nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        return sorted(nums, key=lambda x: x == 0)
