"""
2206. Divide Array Into Equal Pairs
https://leetcode.com/problems/divide-array-into-equal-pairs/
"""


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(nums.count(num) % 2 == 0 for num in nums)
