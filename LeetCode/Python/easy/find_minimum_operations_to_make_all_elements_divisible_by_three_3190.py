"""
3190. Find Minimum Operations to Make All Elements Divisible by Three
https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num % 3 != 0:
                count += 1
        return count
