"""
2869. Minimum Operations to Collect Elements
https://leetcode.com/problems/minimum-operations-to-collect-elements/
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        desired, current = set(range(1, k + 1)), set()
        count = 0
        while not desired.issubset(current):
            current.add(nums.pop())
            count += 1
        return count
