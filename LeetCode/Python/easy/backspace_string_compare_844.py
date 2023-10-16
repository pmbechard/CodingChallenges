"""
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = t_stack = ''
        i = 0
        while i < max(len(s), len(t)):
            if i < len(s):
                if s[i] == '#':
                    if s_stack:
                        s_stack = s_stack[:-1]
                else:
                    s_stack += s[i]
            if i < len(t):
                if t[i] == '#':
                    if t_stack:
                        t_stack = t_stack[:-1]
                else:
                    t_stack += t[i]
            i += 1
        return s_stack == t_stack
