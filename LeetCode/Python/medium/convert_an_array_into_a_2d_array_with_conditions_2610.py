"""
2610. Convert an Array Into a 2D Array With Conditions
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
"""


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []
        while nums:
            nums_set = set(nums)
            result.append(list(nums_set))
            for num in nums_set:
                nums.remove(num)
        return result
