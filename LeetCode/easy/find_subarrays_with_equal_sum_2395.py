"""
2395. Find Subarrays With Equal Sum
https://leetcode.com/problems/find-subarrays-with-equal-sum/
"""


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = []
        for i in range(len(nums) - 1):
            total = sum(nums[i: i + 2])
            if total in sums:
                return True
            else:
                sums.append(total)
        return False
