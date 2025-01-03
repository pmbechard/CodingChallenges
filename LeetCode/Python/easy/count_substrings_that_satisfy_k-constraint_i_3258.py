"""
3258. Count Substrings That Satisfy K-Constraint I
https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/
"""


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        zeros = ones = count = 0
        for i in range(len(s)):
            zeros = ones = 0
            for j in range(i, len(s)):
                if s[j] == '1':
                    ones += 1
                else:
                    zeros += 1
                if zeros <= k or ones <= k:
                    count += 1
                else:
                    break
        return count

