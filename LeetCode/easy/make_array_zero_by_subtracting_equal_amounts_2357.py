"""
2357. Make Array Zero by Subtracting Equal Amounts
https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set([x for x in nums if x != 0]))
