"""
3718. Smallest Missing Multiple of K
https://leetcode.com/problems/smallest-missing-multiple-of-k/
"""


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        div = 0
        while True:
            div += k
            if div not in nums:
                return div
