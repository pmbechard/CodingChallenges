"""
3079. Find the Sum of Encrypted Integers
https://leetcode.com/problems/find-the-sum-of-encrypted-integers
"""


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum([int(max(str(num)) * len(str(num))) for num in nums])
