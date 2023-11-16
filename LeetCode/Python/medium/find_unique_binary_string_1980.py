"""
1980. Find Unique Binary String
https://leetcode.com/problems/find-unique-binary-string
"""


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        for i in range(2 ** length):
            num = f'{bin(i)[2:]}'.zfill(length)
            if num not in nums:
                return num
