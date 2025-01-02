"""
3392. Count Subarrays of Length Three With a Condition
https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/
"""


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 2] == nums[i + 1] / 2:
                count += 1
        return count
