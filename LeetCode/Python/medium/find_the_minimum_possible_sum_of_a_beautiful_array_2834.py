"""
2834. Find the Minimum Possible Sum of a Beautiful Array
https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/
"""


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        total = length = 0
        counter = 1
        while length < n:
            if counter <= target - counter or counter >= target:
                total += counter
                length += 1
            counter += 1
        return total
