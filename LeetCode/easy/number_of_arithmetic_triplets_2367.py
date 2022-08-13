"""
2367. Number of Arithmetic Triplets
https://leetcode.com/problems/number-of-arithmetic-triplets/
"""


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if nums[i] + diff in nums and nums[i] + diff * 2 in nums:
                counter += 1
            elif nums[i] + diff * 2 > nums[-1]:
                break
        return counter
