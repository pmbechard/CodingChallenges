"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest_container = 0
        l, r = 0, len(height) - 1
        while l < r:
            current = min(height[l], height[r]) * (r - l)
            if current > largest_container:
                largest_container = current
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return largest_container
