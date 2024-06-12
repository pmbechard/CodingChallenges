"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = current = 0
        high = len(nums) - 1
        while current <= high:
            if nums[current] == 0:
                if current == low:
                    current += 1
                    low += 1
                else:
                    nums[current], nums[low] = nums[low], nums[current]
                    low += 1
            elif nums[current] == 2:
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1
            else:
                current += 1
            print(nums)
        return nums
