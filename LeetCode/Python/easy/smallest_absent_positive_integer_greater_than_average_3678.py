"""
3678. Smallest Absent Positive Greater Than Average
https://leetcode.com/problems/smallest-absent-positive-greater-than-average/
"""


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        nums = set(nums)
        for num in range(max(1, int(avg)), max(nums)):
            if num not in nums and num > avg:
                return num
        return max(1, max(nums) + 1)
