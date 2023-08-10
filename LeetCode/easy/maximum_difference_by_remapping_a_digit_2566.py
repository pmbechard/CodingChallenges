"""
2566. Maximum Difference by Remapping a Digit
https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        nums = list(set([int(i) for i in str(num)]))
        diffs = []
        for n in nums:
            diffs.append(int(str(num).replace(str(n), '9')))
            diffs.append(int(str(num).replace(str(n), '0')))
        diffs.sort()
        return diffs[-1] - diffs[0]
