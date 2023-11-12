"""
1752. Check if Array Is Sorted and Rotated
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        # target = sorted(nums)
        # for i in range(len(nums)):
        #     if nums[i:] + nums[:i] == target:
        #         return True
        # return False

        count, n = 0, len(nums)
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1
