"""
1913. Maximum Product Difference Between Two Pairs
https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        lowest = nums.pop(nums.index(min(nums)))
        lowest *= nums.pop(nums.index(min(nums)))
        largest = nums.pop(nums.index(max(nums)))
        largest *= nums.pop(nums.index(max(nums)))
        return largest - lowest
