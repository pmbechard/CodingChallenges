"""
3561. Resulting String After Adjacent Removals
https://leetcode.com/problems/resulting-string-after-adjacent-removals/
"""


class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            curr = s[i]
            if not stack:
                stack.append(curr)
                continue
            diff = abs(ord(curr) - ord(stack[-1]))
            if diff == 1 or diff == 25:
                stack.pop()
            else:
                stack.append(curr)
        return ''.join(stack)
