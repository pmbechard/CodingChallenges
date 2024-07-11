"""
1190. Reverse Substrings Between Each Pair of Parentheses
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        left_queue = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                left_queue.append(i)
                i += 1
            elif s[i] == ')':
                l = left_queue.pop()
                s = s[:l] + s[l + 1: i][::-1] + s[i + 1:]
                i -= 1
            else:
                i += 1
        return s
