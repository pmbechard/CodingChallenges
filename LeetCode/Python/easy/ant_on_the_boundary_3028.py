"""
3028. Ant on the Boundary
https://leetcode.com/problems/ant-on-the-boundary
"""


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = count = 0
        for num in nums:
            pos += num
            if pos == 0:
                count += 1
        return count
