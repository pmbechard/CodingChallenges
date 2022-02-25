"""
1588. Sum of All Odd Length Subarrays
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
"""


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            result += arr[i]
            diff = i + 3
            while diff <= len(arr):
                result += sum(arr[i:diff])
                diff += 2
        return result
