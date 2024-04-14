"""
3069. Distribute Elements Into Two Arrays I
https://leetcode.com/problems/distribute-elements-into-two-arrays-i
"""


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        arr1 = [nums.pop()]
        arr2 = [nums.pop()]
        while nums:
            if arr1[-1] > arr2[-1]:
                arr1.append(nums.pop())
            else:
                arr2.append(nums.pop())
        return arr1 + arr2
