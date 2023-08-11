"""
2605. Form Smallest Number From Two Digit Arrays
https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/
"""


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        set_nums = set(nums1).intersection(nums2)
        if len(set_nums) > 0: return min(set_nums)
        min1, min2 = min(nums1), min(nums2)
        return int(f'{min1}{min2}') if min1 < min2 else int(f'{min2}{min1}')
