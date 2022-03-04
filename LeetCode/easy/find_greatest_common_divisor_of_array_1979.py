"""
1979. Find Greatest Common Divisor of Array
https://leetcode.com/problems/find-greatest-common-divisor-of-array/
"""


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        divisor = smallest
        while divisor >= 1:
            if smallest % divisor == 0 and largest % divisor == 0:
                return divisor
            divisor -= 1
