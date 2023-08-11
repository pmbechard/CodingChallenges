"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        seq = 0
        curr = 0
        nums = sorted(list(set(nums)))
        for i in range(len(nums) - 1):
            if abs(nums[i + 1] - nums[i]) == 1:
                curr += 1
                seq = max(curr, seq)
            else:
                curr = 0
        return seq + 1
