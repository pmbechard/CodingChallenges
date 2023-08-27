"""
2829. Determine the Minimum Sum of a k-avoiding Array
https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/
"""


class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        current = counter = 1
        total = 0
        while counter <= n:
            if k // 2 >= current or current >= k:
                total += current
                counter += 1
            current += 1
        return total
