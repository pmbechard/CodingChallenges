"""
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 2
        length = len(nums)
        while curr < length:
            if nums[curr] == nums[curr - 1] == nums[curr - 2]:
                to_remove = nums[curr]
                for i in range(curr + 1, len(nums)):
                    nums[i - 1] = nums[i]
                nums[-1] = to_remove
                length -= 1
            else:
                curr += 1
        return length
