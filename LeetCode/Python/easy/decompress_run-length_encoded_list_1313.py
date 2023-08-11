"""
1313. Decompress Run-Length Encoded List
https://leetcode.com/problems/decompress-run-length-encoded-list/
"""


class Solution:
    def decompressRLElist(self, nums):
        result = []
        for i in range(0, len(nums), 2):
            result += nums[i] * [nums[i + 1]]
        return result
