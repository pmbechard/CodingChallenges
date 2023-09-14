"""
413. Arithmetic Slices
https://leetcode.com/problems/arithmetic-slices/
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        diff = nums[1] - nums[0]
        diff_counter = 2
        result = 0
        current_combs = 0
        for i in range(1, len(nums) - 1):
            if nums[i + 1] - nums[i] == diff:
                diff_counter += 1
                if diff_counter >= 3:
                    current_combs = ((diff_counter - 1) * (diff_counter - 2)) // 2
            else:
                result += current_combs
                current_combs = 0
                diff = nums[i + 1] - nums[i]
                diff_counter = 2
        return max(result, current_combs + result)
