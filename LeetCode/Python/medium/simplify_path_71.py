"""
71. Simplify Path
https://leetcode.com/problems/simplify-path/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if not p or p == '.':
                continue
            elif p == '..':
                if stack: stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)

