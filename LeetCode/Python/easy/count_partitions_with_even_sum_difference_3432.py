"""
3432. Count Partitions with Even Sum Difference
https://leetcode.com/problems/count-partitions-with-even-sum-difference/
"""


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0
