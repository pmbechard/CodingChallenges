"""
2980. Check if Bitwise OR Has Trailing Zeros
https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/
"""


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return any(bin(comb[0] | comb[1])[-1] == '0' for comb in combinations(nums, 2))
