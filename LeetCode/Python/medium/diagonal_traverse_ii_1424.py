"""
1424. Diagonal Traverse II
https://leetcode.com/problems/diagonal-traverse-ii/
"""


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                dic[i + j] = dic.get(i + j, []) + [nums[i][j]]
        output = []
        for i in dic.items():
            output.extend(i[1][::-1])
        return output
