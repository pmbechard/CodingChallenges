"""
3487. Maximum Unique Subarray Sum After Deletion
https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
"""


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        numset = [num for num in set(nums) if num > 0]
        return sum(numset) if numset else max(nums)
