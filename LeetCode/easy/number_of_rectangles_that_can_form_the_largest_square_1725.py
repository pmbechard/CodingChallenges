"""
1725. Number Of Rectangles That Can Form The Largest Square
https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square
"""


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxes = [min(x) for x in rectangles]
        return maxes.count(max(maxes))
