"""
485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        largest = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > largest:
                    largest = count
            else:
                count = 0
        return largest
