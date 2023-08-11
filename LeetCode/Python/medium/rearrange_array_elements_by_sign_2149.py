"""
2149. Rearrange Array Elements by Sign
https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_nums = [i for i in nums if i > 0]
        neg_nums = [i for i in nums if i < 0]
        result = []
        for i in range(len(pos_nums)):
            result.append(pos_nums[i])
            result.append(neg_nums[i])
        return result
