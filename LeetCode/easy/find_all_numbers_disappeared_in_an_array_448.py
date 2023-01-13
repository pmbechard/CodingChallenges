"""
448. Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(list(range(1, len(nums)+1))).difference(nums))
