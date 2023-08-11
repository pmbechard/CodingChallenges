"""
2455. Average Value of Even Numbers That Are Divisible by Three
https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
"""


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        nums = [num for num in nums if num % 6 == 0]
        if len(nums) == 0: return 0
        return floor(sum(nums) / len(nums))
