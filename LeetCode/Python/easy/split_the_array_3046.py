"""
3046. Split the Array
https://leetcode.com/problems/split-the-array/
"""


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return Counter(nums).most_common(1)[0][1] < 3
