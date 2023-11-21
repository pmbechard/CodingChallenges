"""
1814. Count Nice Pairs in an Array
https://leetcode.com/problems/count-nice-pairs-in-an-array/
"""


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dic = dict()
        pairs = 0
        for num in nums:
            total = num - int(str(num)[::-1])
            dic[total] = dic.get(total, 0) + 1
            if dic[total] > 1:
                pairs += dic[total] - 1
        return pairs % (10 ** 9 + 7)
