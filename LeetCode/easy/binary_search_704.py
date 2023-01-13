"""
704. Binary Search
https://leetcode.com/problems/binary-search/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        orig = nums[:]
        while len(nums) > 0:
            mid = len(nums)//2
            if nums[mid] == target:
                return orig.index(nums[mid])
            elif nums[mid] > target:
                nums = nums[:mid]
            else:
                nums = nums[mid+1:]
        return -1
