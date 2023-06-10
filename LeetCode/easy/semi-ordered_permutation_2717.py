"""
2717. Semi-Ordered Permutation
https://leetcode.com/problems/semi-ordered-permutation/
"""


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        counter = 0
        while nums[0] != 1 or nums[-1] != len(nums):
            if nums[0] != 1:
                i = nums.index(1)
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                counter += 1

            if nums[-1] != len(nums):
                i = nums.index(len(nums))
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                counter += 1

        return counter
