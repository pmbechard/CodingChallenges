"""
2341. Maximum Number of Pairs in Array
https://leetcode.com/problems/maximum-number-of-pairs-in-array/
"""


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        leftover = len(set([x for x in nums if nums.count(x) % 2 == 1]))
        pairs = (len(nums) - leftover) // 2
        return [pairs, leftover]
