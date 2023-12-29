"""
2970. Count the Number of Incremovable Subarrays I
https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/
"""


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sub = nums[:i] + nums[j:]
                if all(a < b for a, b in zip(sub, sub[1:])):
                    count += 1
        return count
