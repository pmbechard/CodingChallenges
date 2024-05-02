"""
2441. Largest Positive Integer That Exists With Its Negative
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
"""


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        visited = set()
        largest = -1
        for i in nums:
            if -i in visited and abs(i) > largest:
                largest = abs(i)
            visited.add(i)
        return largest
