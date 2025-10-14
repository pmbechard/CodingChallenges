"""
3712. Sum of Elements With Frequency Divisible by K
https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/
"""


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        ctr = Counter(nums)
        output = 0
        for i, f in ctr.items():
            if f % k == 0:
                output += i * f
        return output
