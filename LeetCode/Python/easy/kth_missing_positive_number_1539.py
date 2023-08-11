"""
1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = set(list(range(1, arr[-1]))).difference(arr)
        if len(missing) >= k:
            return sorted(list(missing))[k-1]
        return arr[-1] + (k - len(missing))
