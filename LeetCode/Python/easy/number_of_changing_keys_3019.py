"""
3019. Number of Changing Keys
https://leetcode.com/problems/number-of-changing-keys
"""


class Solution:
    def countKeyChanges(self, s: str) -> int:
        stack = []
        for c in s.lower():
            if not stack or stack[-1] != c:
                stack.append(c)
        return len(stack) - 1
