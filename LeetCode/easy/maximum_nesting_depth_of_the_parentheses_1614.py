"""
1614. Maximum Nesting Depth of the Parentheses
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        if s == '()':
            return 1
        for i in range(len(s)):
            if s[i] == '(':
                index = i + 1
                pars = 1
                while index < len(s):
                    if s[index] == '(':
                        pars += 1
                    elif s[index] == ')':
                        pars -= 1
                    index += 1
                    if pars > result:
                        result = pars
        return result
