"""
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums
        result = []
        start = end = nums[0]
        for i in range(len(nums)):
            if i + 1 == len(nums) or nums[i + 1] - nums[i] != 1:
                if start == end:
                    result.append(f'{start}')
                else:
                    result.append(f'{start}->{end}')
                if i + 1 < len(nums):
                    start = end = nums[i + 1]
            else:
                end = nums[i + 1]
        return result
