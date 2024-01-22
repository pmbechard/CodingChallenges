"""
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [Counter(nums).most_common(1).pop()[0], set(range(1, len(nums) + 1)).difference(nums).pop()]
