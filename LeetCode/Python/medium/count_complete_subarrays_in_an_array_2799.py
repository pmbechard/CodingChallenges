"""
2799. Count Complete Subarrays in an Array
https://leetcode.com/problems/count-complete-subarrays-in-an-array/
"""


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        distinct = len(set(nums))
        for i in range(length):
            subarr = set()
            for j in range(i, length):
                subarr.add(nums[j])
                if len(subarr) == distinct:
                    count += 1
        return count
