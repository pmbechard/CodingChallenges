"""
575. Distribute Candies
https://leetcode.com/problems/distribute-candies/
"""


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
