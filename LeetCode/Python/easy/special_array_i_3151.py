"""
3151. Special Array I
https://leetcode.com/problems/special-array-i/
"""


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev_even = nums[0] % 2 == 0
        for num in nums[1:]:
            if (num % 2 == 0) == prev_even:
                return False
            prev_even = not prev_even
        return True
