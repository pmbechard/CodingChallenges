"""
1758. Minimum Changes To Make Alternating Binary String
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
"""


class Solution:
    def minOperations(self, s: str) -> int:
        op1 = op2 = 0
        is_even = True
        for i in range(len(s)):
            if is_even:
                if s[i] == '1':
                    op1 += 1
                else:
                    op2 += 1
            else:
                if s[i] == '1':
                    op2 += 1
                else:
                    op1 += 1
            is_even = not is_even
        return min(op1, op2)
