"""
1021. Remove Outermost Parentheses
https://leetcode.com/problems/remove-outermost-parentheses/
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter  = 0
        start = 0
        result = ""
        for i in range(len(s)):
            if s[i] == '(':
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                result += s[start+1:i]
                start = i + 1
        return result
