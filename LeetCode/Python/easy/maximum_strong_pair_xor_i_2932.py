"""
2932. Maximum Strong Pair XOR I
https://leetcode.com/problems/maximum-strong-pair-xor-i/
"""


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        lg = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y) and x ^ y > lg:
                    lg = x ^ y
        return lg
