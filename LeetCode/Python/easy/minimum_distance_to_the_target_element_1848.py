"""
1848. Minimum Distance to the Target Element
https://leetcode.com/problems/minimum-distance-to-the-target-element/
"""


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        try:
            return min(nums[start:].index(target), nums[::-1][len(nums) - 1 - start:].index(target))
        except:
            try:
                return nums[start:].index(target)
            except:
                return nums[::-1][len(nums) - 1 - start:].index(target)
