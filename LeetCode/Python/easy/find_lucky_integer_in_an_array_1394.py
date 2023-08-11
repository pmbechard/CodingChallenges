"""
1394. Find Lucky Integer in an Array
https://leetcode.com/problems/find-lucky-integer-in-an-array/
"""


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        largest = -1
        for num in set(arr):
            if num == arr.count(num) and num > largest:
                largest = num
        return largest
