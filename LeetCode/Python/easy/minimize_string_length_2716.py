"""
2716. Minimize String Length
https://leetcode.com/problems/minimize-string-length/
"""


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
