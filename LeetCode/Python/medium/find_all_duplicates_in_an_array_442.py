"""
442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        results = []
        for num in nums:
            if dic.get(num):
                results.append(num)
            else:
                dic[num] = 1
        return results
