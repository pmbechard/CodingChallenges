"""
2574. Left and Right Sum Differences
https://leetcode.com/problems/left-and-right-sum-differences/
"""


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        sums = [0] * len(nums)
        left_sum = right_sum = 0
        for i in range(len(nums)):
            left = i
            right = len(nums) - 1 - i

            sums[left] = abs(sums[left] - left_sum)
            sums[right] = abs(sums[right] - right_sum)

            left_sum += nums[left]
            right_sum += nums[right]
        return sums
