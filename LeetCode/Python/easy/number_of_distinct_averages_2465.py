"""
2465. Number of Distinct Averages
https://leetcode.com/problems/number-of-distinct-averages/
"""


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avgs = []
        nums.sort()
        while nums:
            avgs.append((nums[0] + nums[-1]) / 2)
            nums = nums[1 : -1]
        return len(set(avgs))
