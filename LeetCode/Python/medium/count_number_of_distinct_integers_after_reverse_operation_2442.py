"""
2442. Count Number of Distinct Integers After Reverse Operations
https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations
"""


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums += [int(str(num)[::-1]) for num in nums]
        return len(set(nums))
