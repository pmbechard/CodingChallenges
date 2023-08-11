"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for k, v in enumerate(s):
            if s.count(v) == 1:
                return k
        return -1
