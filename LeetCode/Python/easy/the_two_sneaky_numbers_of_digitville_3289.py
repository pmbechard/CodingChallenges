"""
3289. The Two Sneaky Numbers of Digitville
https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
"""


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [i[0] for i in Counter(nums).most_common(2)]
