"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted(set(nums), key=lambda x: nums.count(x))[-k:]
