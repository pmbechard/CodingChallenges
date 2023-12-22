"""
1422. Maximum Score After Splitting a String
https://leetcode.com/problems/maximum-score-after-splitting-a-string/
"""


class Solution:
    def maxScore(self, s: str) -> int:
        l = 1 if s[0] == '0' else 0
        r = s[1:].count('1')
        total = r + l
        for i in range(1, len(s) - 1):
            if s[i] == '1':
                r -= 1
            else:
                l += 1
            if r + l > total:
                total = r + l
        return total
