"""
2475. Number of Unequal Triplets in Array
https://leetcode.com/problems/number-of-unequal-triplets-in-array/
"""


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return 0
        elif len(nums) == 3:
            return 1

        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1
        return count
