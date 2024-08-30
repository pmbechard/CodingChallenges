"""
3264. Final Array State After K Multiplication Operations I
https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
"""


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            n = min(nums)
            nums[nums.index(n)] = n * multiplier
        return nums
