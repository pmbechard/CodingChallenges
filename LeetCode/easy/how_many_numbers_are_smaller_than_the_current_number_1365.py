"""
1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        results = []
        for i in nums:
            results.append(len([x for x in nums if x < i]))
        return results
