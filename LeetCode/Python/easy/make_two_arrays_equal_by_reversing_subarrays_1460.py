"""
1460. Make Two Arrays Equal by Reversing Subarrays
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
"""


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
