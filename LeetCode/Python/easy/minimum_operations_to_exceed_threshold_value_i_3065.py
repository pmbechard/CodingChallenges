"""
3065. Minimum Operations to Exceed Threshold Value I
https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        for num in nums:
            if num >= k:
                return count
            count += 1
