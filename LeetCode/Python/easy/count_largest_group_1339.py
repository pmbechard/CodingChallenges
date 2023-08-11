"""
1399. Count Largest Group
https://leetcode.com/problems/count-largest-group/
"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums = dict()
        max_count = max_len = 0
        for i in range(1, n + 1):
            i_sum = sum([int(x) for x in str(i)])
            sums[i_sum] = sums.get(i_sum, 0) + 1
        sums_list = list(sums.values())
        return sums_list.count(max(set(sums_list)))
