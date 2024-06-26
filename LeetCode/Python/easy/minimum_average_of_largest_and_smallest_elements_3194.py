"""
3194. Minimum Average of Smallest and Largest Elements
https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
"""


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        min_avg = math.inf
        nums.sort()
        offset = 0
        while offset < len(nums) - offset:
            min_avg = min(min_avg, (nums[offset] + nums[-offset - 1]) / 2)
            offset += 1
        return min_avg
