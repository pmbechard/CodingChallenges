"""
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = list(set(range(1, len(nums) + 1)).difference(nums))[0]
        double = sum(nums) - sum(set(nums))
        return [double, missing]
