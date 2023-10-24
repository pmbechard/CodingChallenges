"""
1576. Replace All ?'s to Avoid Consecutive Repeating Characters
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
"""


class Solution:
    def modifyString(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] == '?':
                neighbours = ''
                if i - 1 >= 0:
                    neighbours += s[i - 1]
                if i + 1 < len(s):
                    neighbours += s[i + 1]
                current = 97
                while chr(current) in neighbours:
                    current += 1
                s = s[:i] + chr(current) + s[i + 1:]
        return s
