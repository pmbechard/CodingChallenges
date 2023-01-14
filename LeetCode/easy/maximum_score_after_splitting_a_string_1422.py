"""
1422. Maximum Score After Splitting a String
https://leetcode.com/problems/maximum-score-after-splitting-a-string/
"""

class Solution:
    def maxScore(self, s: str) -> int:
        total = 0
        for i in range(1, len(s)):
            current = s[:i].count('0') + s[i:].count('1')
            if current > total:
                total = current
        return total

