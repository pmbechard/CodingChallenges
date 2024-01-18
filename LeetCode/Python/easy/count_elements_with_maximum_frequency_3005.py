"""
3005. Count Elements With Maximum Frequency
https://leetcode.com/problems/count-elements-with-maximum-frequency
"""


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        most_common = max(counter.values())
        return sum([i for i in counter.values() if i == most_common])
