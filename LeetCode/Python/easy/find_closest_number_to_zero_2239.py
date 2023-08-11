"""
2239. Find Closest Number to Zero
https://leetcode.com/problems/find-closest-number-to-zero/
"""


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        output = None
        for i in nums:
            if output == None:
                output = i
            elif abs(i) == abs(output):
                output = max(i, output)
            elif abs(i) < abs(output):
                output = i
        return output
