"""
922. Sort Array By Parity II
https://leetcode.com/problems/sort-array-by-parity-ii/
"""


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, key=lambda x: x % 2 == 1)
        even = nums[:len(nums)//2]
        odd = nums[len(nums)//2:]
        results = []
        for i in range(len(even)):
            results.append(even[i])
            results.append(odd[i])
        return results
