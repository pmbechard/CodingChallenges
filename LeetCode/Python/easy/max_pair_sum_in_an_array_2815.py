"""
2815. Max Pair Sum in an Array
https://leetcode.com/problems/max-pair-sum-in-an-array/
"""


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic = dict()
        max_sum = None
        for num in nums:
            max_num = str(max([int(i) for i in str(num)]))
            dic[max_num] = dic.get(max_num, []) + [num]
            if len(dic[max_num]) > 2:
                dic[max_num] = sorted(dic[max_num])[-2:]
            if len(dic[max_num]) == 2:
                curr_sum = sum(dic[max_num])
                if not max_sum or curr_sum > max_sum:
                    max_sum = curr_sum
        if not max_sum:
            return -1
        return max_sum
