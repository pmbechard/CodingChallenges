"""
2640. Find the Score of All Prefixes of an Array
https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/
"""


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        acc = 0
        result = []
        curr_max = 0
        for i in range(len(nums)):
            acc += nums[i]
            if nums[i] > curr_max:
                curr_max = nums[i]
            acc += curr_max
            result.append(acc)
        return result
