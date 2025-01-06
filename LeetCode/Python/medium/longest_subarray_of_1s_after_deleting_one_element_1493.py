"""
1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            if nums[0] == 1:
                return len(nums) - 1
            return 0

        curr = 0
        prev = 0
        lg = 0
        prev_gap = False

        for num in nums:
            if num == 1:
                prev_gap = False
                curr += 1
            elif num == 0:
                prev = 0 if prev_gap else curr
                curr = 0
                prev_gap = True
            lg = max(lg, prev + curr)
        return lg
