"""
2161. Partition Array According to Given Pivot
https://leetcode.com/problems/partition-array-according-to-given-pivot/
"""


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [i for i in nums if i < pivot]
        greater = [i for i in nums if i > pivot]
        return less + [pivot] * nums.count(pivot) + greater
