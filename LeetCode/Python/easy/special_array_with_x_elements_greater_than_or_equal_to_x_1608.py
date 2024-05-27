"""
1608. Special Array With X Elements Greater Than or Equal X
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        nums_idx = 0
        for i in range(nums[-1] + 1):
            while nums[nums_idx] < i:
                nums_idx += 1
                if nums_idx == len(nums):
                    break
            greater_than = len(nums) - nums_idx
            if greater_than == i:
                return i
        return -1
