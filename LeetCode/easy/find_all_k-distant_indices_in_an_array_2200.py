"""
2200. Find All K-Distant Indices in an Array
https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
"""


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        results = []
        for x in range(len(nums)):
            if nums[x] == key:
                results += list(range(max(0, x - k), min(len(nums), x + k + 1)))
        return set(results)
