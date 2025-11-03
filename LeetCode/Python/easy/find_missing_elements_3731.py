"""
3731. Find Missing Elements
https://leetcode.com/problems/find-missing-elements/
"""


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = maxi = nums[0]
        for num in nums:
            if num < mini:
                mini = num
            elif num > maxi:
                maxi = num
        result = []
        nums = set(nums)
        for num in range(mini, maxi + 1):
            if num not in nums:
                result.append(num)
        return result
