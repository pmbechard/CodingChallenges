"""
2023. Number of Pairs of Strings With Concatenation Equal to Target
https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/submissions/925887285/
"""


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if nums[i] + nums[j] == target:
                    output += 1
        return output
