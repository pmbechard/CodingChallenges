"""
2997. Minimum Number of Operations to Make Array XOR Equal to K
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        max_len = max(len(bin(k)), len(bin(xor))) - 2
        bin_k, bin_xor = bin(k)[2:].zfill(max_len), bin(xor)[2:].zfill(max_len)
        return sum([1 if bin_k[i] != bin_xor[i] else 0 for i in range(len(bin_k))])
