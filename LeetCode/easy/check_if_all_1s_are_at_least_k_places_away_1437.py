"""
1437. Check If All 1's Are at Least Length K Places Away
https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
"""


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        indices = [i for i in range(len(nums)) if nums[i] == 1]
        for i in range(len(indices) - 1):
            if indices[i+1] - indices[i] <= k:
                return False
        return True
