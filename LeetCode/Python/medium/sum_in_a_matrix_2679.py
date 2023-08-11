"""
2679. Sum in a Matrix
https://leetcode.com/problems/sum-in-a-matrix/
"""


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        nums = [sorted(row) for row in nums]
        score = index = 0
        for col in range(len(nums[0])):
            score += max([row[index] for row in nums])
            index += 1
        return score
